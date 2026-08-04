
from fastapi import FastAPI,Request,HTTPException, Response,status,Depends,APIRouter
from passlib.context import CryptContext
from sqlalchemy.orm import Session, session
from .. database import engine, get_db
from typing import List, Optional
from .. import models, schemas

router = APIRouter(
     prefix="/sqlalchemy/courses"
)

#insert data 
@router.post('/', response_model=schemas.SQLCourseResponse)
def create_course(course:schemas.SQLCourseCreate, db:Session = Depends(get_db)):
    new_course = models.Course(**course.model_dump()) #convert pyathn object to dictionary using model_dump() method
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

#get data 
#get data 
@router.get('/', response_model=List[schemas.SQLCourseResponse])
def get_courses(db:Session = Depends(get_db)):
    courses = db.query(models.Course).all()
    return courses

#get single data 
@router.get('/{course_id}', response_model=schemas.SQLCourseResponse)
def get_course(course_id:int, db:Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()

    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Course id : {course_id} not found")
    return course

#update single course
#update single course
@router.put('/{course_id}', response_model=schemas.SQLCourseResponse)
def update_course(course_id:int, course_data:schemas.SQLCourseCreate, db:Session = Depends(get_db)):
    course_query = db.query(models.Course).filter(models.Course.id==course_id)
    course = course_query.first()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Course id : {course_id} not found")

    course_query.update(
        course_data.model_dump(),
        synchronize_session=False
    )
    db.commit()
    updated_course = course_query.first()
    return  updated_course

#delete single course
#delete single course
@router.delete('/{course_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id:int, db:Session = Depends(get_db)):
    existing_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not existing_course:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Course id : {course_id} not found"
            )
    db.delete(existing_course)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

