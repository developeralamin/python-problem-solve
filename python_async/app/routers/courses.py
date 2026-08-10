from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_db
from .. import models
from .. import schemas

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

@router.get("/")
async def get_courses(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Course))
    courses = result.scalars().all()
    return courses

@router.post("/")
async def create_course(
    course: schemas.SQLCourseCreate,
    db: AsyncSession = Depends(get_db)
):
    new_course = models.Course(
        **course.model_dump()
    )
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)

    return new_course