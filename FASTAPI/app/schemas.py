
from datetime import datetime

from pydantic import BaseModel,EmailStr, Field

class SQLCourseCreate(BaseModel):
    name:str
    description:str
    instructor:str

class SQLCourseResponse(SQLCourseCreate):
    id: int
    name: str
    description: str
    instructor: str
   
   #second way inheritance 
    # class Config:
    #     orm_mode = True

class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
   password: str = Field(
        min_length=8,
        max_length=72
    )

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True,
        extra="forbid" #if the column doesn;t exists
        frozen=True
        validate_assignment=True
        anystr_strip_whitespace=True

class UserLogin(UserBase):
    password: str = Field(
        min_length=8,
        max_length=72
    )