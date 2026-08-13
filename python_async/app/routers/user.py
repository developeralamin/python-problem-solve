from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..email import send_verification_email

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
    new_user = models.User(
        **user.model_dump()
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    # verification 
    verification_token = 'temporay-token'
    background_tasks.add_task(
        send_verification_email,
        new_user.email,
        verification_token
    )
    return new_user