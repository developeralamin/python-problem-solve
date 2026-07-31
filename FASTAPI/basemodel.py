import time

import psycopg2

from fastapi import FastAPI,Request,HTTPException, Response,status
from pydantic import BaseModel
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from psycopg2.extras import RealDictCursor

app = FastAPI()
class User(BaseModel):
    id: int
    name: str
    email: str

class Course(BaseModel):
    name: str
    time: str


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

@app.get("/")
def root():
    return {"message": "Hello Alamin"}

@app.get("/alamin")
def read_alamin():
    return {"message": "Hello Alamin"}

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

