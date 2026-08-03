import time

import psycopg2

from fastapi import FastAPI,Request,HTTPException, Response,status,Depends
from pydantic import BaseModel
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from psycopg2.extras import RealDictCursor
from passlib.context import CryptContext


# from FASTAPI.app import schemas
from . import models
from sqlalchemy.orm import Session, session
from . database import engine, get_db
from . import schemas
from typing import List, Optional

app = FastAPI()

# //create  tables from all metadata of models.py
models.Base.metadata.create_all(bind=engine)



class User(BaseModel):
    id: int
    name: str
    email: str

class Course(BaseModel):
    name: str
    time: str

#define request body schema for SQLAlchemy ORM


while True:
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="root",
            cursor_factory=RealDictCursor)
        cursor = connection.cursor()
        print("Database connection was successful!")
        break

    except Exception as e:
        print("Database connection failed. Retrying in 5 seconds...")
        print(f"Error: {e}")
        time.sleep(2)


# //call database connection
@app.get('/list')
def coure_list():
    cursor.execute("SELECT * FROM courses")
    data = cursor.fetchall()
    return {"success": True, "data": data}

# //store data in database
@app.post("/courses/")
def create_course(course: Course):
    cursor.execute("INSERT INTO courses (name, time) VALUES (%s, %s)", (course.name, course.time))
    connection.commit()
    return {
        "success": True,
        "message": "Course created successfully.",
        "data": course
    }

# //single data from db
@app.get('/courses/{course_id}')
def get_course(course_id: int):
    cursor.execute("SELECT * FROM courses WHERE id = %s", (course_id,))
    data = cursor.fetchone()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Course not found")
    return {"success": True, "data": data}

@app.put('/courses/{course_id}')
def update_course(course_id: int, course: Course):
    cursor.execute("UPDATE courses SET name = %s, time = %s WHERE id = %s returning *", (course.name, course.time, course_id))
    update_course = cursor.fetchone()
    connection.commit()
    if update_course == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Course with id: {course_id} not found")
    return {
            "success": True,
            "message": "Course updated successfully.",
            "data": update_course
        }

# // //delete data from db
@app.delete('/courses/{course_id}')
def delete_course(course_id: int):
    cursor.execute("DELETE FROM courses where id = %s returning *", (str(course_id),))
    deleted_course = cursor.fetchone()
    connection.commit()

    if deleted_course == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Course with id: {course_id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("/users/")
def create_user(user: User):
    return {
        "success": True,
        "message": "User created successfully.",
        "data": user
    }

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for err in exc.errors():
        errors.append({
            "field": ".".join(str(x) for x in err["loc"][1:]),  # body -> name => name
            "message": err["msg"],
            "type": err["type"],
            "input": err.get("input")
        })

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation Error",
            "errors": errors
        }
    )



# //create table in sqlalchemy orm
# //create table in sqlalchemy orm
# //create table in sqlalchemy orm

@app.get('/sqlalchemy')
def course(db:session  = Depends(get_db)):
    return {"message": "sqlalchemy ORM Working"}

#insert data 
@app.post('/sqlalchemy/courses', response_model=schemas.SQLCourseResponse)
def create_course(course:schemas.SQLCourseCreate, db:Session = Depends(get_db)):
    new_course = models.Course(**course.model_dump()) #convert pyathn object to dictionary using model_dump() method
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

#get data 
#get data 
@app.get('/sqlalchemy/courses', response_model=List[schemas.SQLCourseResponse])
def get_courses(db:Session = Depends(get_db)):
    courses = db.query(models.Course).all()
    return courses

#get single data 
@app.get('/sqlalchemy/courses/{course_id}', response_model=schemas.SQLCourseResponse)
def get_course(course_id:int, db:Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()

    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Course id : {course_id} not found")
    return course

#update single course
#update single course
@app.put('/sqlalchemy/courses/{course_id}', response_model=schemas.SQLCourseResponse)
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
@app.delete('/sqlalchemy/courses/{course_id}', status_code=status.HTTP_204_NO_CONTENT)
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


#user create
@app.post('/sqlalchemy/users', status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate, db:Session = Depends(get_db)):
    new_user = models.User(**user.model_dump())
    exising_user = db.query(models.User).filter(models.User.email == user.email).first()
    if exising_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"User with email: {user.email} already exists"
        )
    hashed_password = CryptContext(schemes=["bcrypt"], deprecated="auto").hash(user.password)
    new_user.password = hashed_password
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user