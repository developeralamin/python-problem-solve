import time

import psycopg2

from fastapi import FastAPI,Request
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

