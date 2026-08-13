from fastapi import FastAPI
from .routers import courses,user

app = FastAPI()

app.include_router(courses.router)
app.include_router(user.router)


