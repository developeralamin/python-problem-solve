from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routers import courses, user
from .database import engine
from . import models

# ১. অ্যাপ চালুর সময় ডাটাবেজ টেবিল তৈরি করার লাইফসাইকেল ফাংশন
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        # মডেলগুলোতে ডিফাইন করা সব টেবিল অটোমেটিক তৈরি করবে
        await conn.run_sync(models.Base.metadata.create_all)
    yield  # এখান থেকে অ্যাপ চলা শুরু করবে

# ২. FastAPI অ্যাপের সাথে lifespan যুক্ত করা
app = FastAPI(lifespan=lifespan)

# ৩. রাউটার অন্তর্ভুক্ত করা
app.include_router(courses.router)
app.include_router(user.router)