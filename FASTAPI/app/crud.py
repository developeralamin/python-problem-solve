
from . routers import user, course,auth
from fastapi import FastAPI
from . import models
from . database import engine

app = FastAPI()

# //create  tables from all metadata of models.py
models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(course.router)
app.include_router(auth.router)