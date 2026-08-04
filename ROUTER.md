FastAPI APIRouter

What is APIRouter?

APIRouter is a FastAPI component used to organize endpoints intoseparate, reusable modules.

Instead of putting every endpoint in main.py, related endpoints aregrouped into router files.

Why use APIRouter?

Without APIRouter:

main.py
 ├── User APIs
 ├── Course APIs
 ├── Auth APIs
 ├── Post APIs
 └── Payment APIs

As the project grows, main.py becomes difficult to maintain.

With APIRouter:

app/
│
├── main.py
├── routers/
│   ├── users.py
│   ├── courses.py
│   ├── auth.py
│   └── posts.py

Each file contains only one feature.

Basic Example

from fastapi import APIRouter

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

@router.get("/")
def get_courses():
    return {"message": "All Courses"}

In main.py:

from fastapi import FastAPI
from app.routers import courses

app = FastAPI()

app.include_router(courses.router)

How include_router() Works

Client Request
      │
      ▼
FastAPI App
      │
      ▼
include_router()
      │
      ▼
Registered Routes
      │
      ▼
Endpoint Function

Prefix

router = APIRouter(prefix="/users")

@router.get("/")

Final URL:

GET /users/

Tags

router = APIRouter(tags=["Users"])

Groups endpoints in Swagger UI.

Shared Dependencies

router = APIRouter(
    prefix="/users",
    dependencies=[Depends(get_current_user)]
)

Every endpoint in the router automatically uses the dependency.

Benefits

Modular code

Cleaner main.py

Feature-based organization

Reusable routers

Shared prefix

Shared dependencies

Better Swagger documentation

Easier teamwork

Recommended Project Structure

app/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── routers/
│   ├── users.py
│   ├── courses.py
│   ├── auth.py
│   └── posts.py
├── services/
├── repositories/
└── core/

Request Flow

Client
   │
   ▼
FastAPI
   │
   ▼
include_router()
   │
   ▼
Router
   │
   ▼
Endpoint
   │
   ▼
Database
   │
   ▼
Response

Summary

APIRouter keeps APIs modular.

include_router() registers routes with the FastAPI app.

prefix avoids repeating URL paths.

tags organize Swagger documentation.

Router-level dependencies reduce duplicate code.

APIRouter is the standard approach for medium and large FastAPIprojects.