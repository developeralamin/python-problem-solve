
from datetime import datetime

from pydantic import BaseModel,EmailStr, Field, field_validator
from typing import Optional

class SQLCourseCreate(BaseModel):
    name:str
    description:str
    instructor:str

class SQLCourseResponse(SQLCourseCreate):
    id: int
    name: str
    description: str
    instructor: str
    user_id: int
   
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

   @field_validator('password')
   @classmethod
   def password_must_fit_bcrypt_bytes(cls, value: str) -> str:
       if len(value.encode('utf-8')) > 72:
           raise ValueError('Password must not exceed 72 bytes in UTF-8 form')
       return value

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
    password: str 

#thise schema is used for only validation purpose, not for database
class Token(BaseModel):
    access_token: str
    token_type: str

#response schema for token data
class TokenData(BaseModel):
    id : Optional[int] = None