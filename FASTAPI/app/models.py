from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, text, ForeignKey
from . database import Base

class Course(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    instructor = Column(String, nullable=True)
    user_id = Column(
            Integer,
            ForeignKey("users.id",ondelete="CASCADE"),
            nullable=False,
        )

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

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, nullable=False)
    email = Column(String, nullable=False, unique = True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))