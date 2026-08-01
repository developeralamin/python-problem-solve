from sqlalchemy import Column, Integer, String, ForeignKey
from . database import Base

class Course(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    instructor = Column(String, nullable=True)

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    course_id = Column(
        Integer,
        ForeignKey("posts.id"),
        nullable=False
    )