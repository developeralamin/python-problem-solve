
import secrets
from datetime import datetime, timedelta, timezone

from fastapi import (
    APIRouter,
    Depends,
    BackgroundTasks,
    HTTPException,
    status,
)
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from ..database import get_db
from .. import models, schemas
from ..email_utils import (
    send_verification_email,
    send_password_reset_email,
)
from ..security import (
    hash_password,
    verify_password,
    hash_token,
    create_access_token,
    RESET_TOKEN_EXPIRE_MINUTES,
)

router = APIRouter(
    prefix="/user",
    tags=["User"],
)


# ---------------- GET USERS ----------------
@router.get("/")
async def get_users(
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(models.User))
    users = result.scalars().all()

    # Never return password hashes or private tokens.
    return [
        {
            "id": user.id,
            "email": user.email,
            "is_verified": user.is_verified,
            "created_at": user.created_at,
        }
        for user in users
    ]


# ---------------- REGISTER ----------------
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: schemas.UserCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(models.User).where(
            models.User.email == user.email
        )
    )

    if result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    verification_token = secrets.token_urlsafe(32)

    new_user = models.User(
        email=user.email,
        password=hash_password(user.password),
        is_verified=False,
        password_verification=hash_token(
            verification_token
        ),
    )

    db.add(new_user)

    try:
        await db.commit()
        await db.refresh(new_user)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    background_tasks.add_task(
        send_verification_email,
        new_user.email,
        verification_token,
    )

    return {
        "message": "Registration successful. Please verify your email.",
        "email": new_user.email,
    }


# ---------------- VERIFY EMAIL ----------------
@router.get("/verify-email")
async def verify_email(
    token: str,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(models.User).where(
            models.User.password_verification
            == hash_token(token)
        )
    )

    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or already used verification token",
        )

    user.is_verified = True
    user.password_verification = None
    await db.commit()
    return {
        "message": "Email verified successfully. You can now log in."
    }


# ---------------- LOGIN ----------------
@router.post("/login", response_model=schemas.Token)
async def login(
    credentials: schemas.UserLogin,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(models.User).where(
            models.User.email == credentials.email
        )
    )

    user = result.scalars().first()
    if (
        not user
        or not verify_password(
            credentials.password,
            user.password,
        )
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Please verify your email before logging in",
        )

    return {
        "access_token": create_access_token(user.id),
        "token_type": "bearer",
    }


# ---------------- FORGOT PASSWORD ----------------
@router.post("/forgot-password")
async def forgot_password(
    data: schemas.ForgotPasswordRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(models.User).where(
            models.User.email == data.email
        )
    )

    user = result.scalars().first()
    # Same response whether the account exists or not.
    response = {
        "message": (
            "If the account exists, password reset instructions "
            "will be sent."
        )
    }

    if not user:
        return response
    reset_token = secrets.token_urlsafe(32)

    user.password_reset_token = hash_token(reset_token)
    user.password_reset_expires = (
        datetime.now(timezone.utc) + timedelta(minutes=15)
    )

    await db.commit()
    # user.password_reset_token = hash_token(reset_token)
    # user.password_reset_expires = (
    #     datetime.now(timezone.utc).replace(tzinfo=None)
    #     + timedelta(minutes=RESET_TOKEN_EXPIRE_MINUTES)
    # )

    # await db.commit()
    background_tasks.add_task(
        send_password_reset_email,
        user.email,
        reset_token,
    )

    return response


# ---------------- RESET PASSWORD ----------------

@router.post("/reset-password")
async def reset_password(
    data: schemas.ResetPasswordRequest,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(models.User).where(
            models.User.password_reset_token
            == hash_token(data.token)
        )
    )

    user = result.scalars().first()

    if not user or not user.password_reset_expires:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired reset token",
        )

    expires = user.password_reset_expires

    # Support databases that return naive datetime values.
    if expires.tzinfo is None:
        expires = expires.replace(tzinfo=timezone.utc)

    if datetime.now(timezone.utc) >= expires:
        user.password_reset_token = None
        user.password_reset_expires = None
        await db.commit()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Reset token expired. Please request a new one.",
        )

    user.password = hash_password(data.new_password)

    # Invalidate the token after successful reset.
    user.password_reset_token = None
    user.password_reset_expires = None

    await db.commit()

    return {
        "message": "Password reset successfully. Please log in."
    }
