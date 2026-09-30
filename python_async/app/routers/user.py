import secrets
from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..email_utils import send_verification_email

from ..database import get_db
from .. import models
from .. import schemas

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get("/")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.User))
    users = result.scalars().all()
    return users


@router.post("/")
async def create_user(
    user: schemas.UserCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    verification_token = secrets.token_urlsafe(32)
    new_user = models.User(
        **user.model_dump(),
        password_verification=verification_token
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    # verification 
    background_tasks.add_task(
        send_verification_email,
        new_user.email,
        verification_token
    )
    return new_user


# --- Query Parameter এর জন্য ফিক্সড রাউট ---
@router.get("/verify-email")
async def verify_email(token: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(models.User).where(models.User.password_verification == token)
    )
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid verification token"
        )
    
    user.is_verified = True
    user.password_verification = None  # DB Field Name
    await db.commit()
    
    return {"message": "Email verified successfully"}