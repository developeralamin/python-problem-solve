
from datetime import datetime
from typing import Optional

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ConfigDict,
    field_validator,
)


# ---------------- COURSE SCHEMAS ----------------

class SQLCourseCreate(BaseModel):
    name: str
    description: Optional[str] = None
    instructor: Optional[str] = None
    user_id: int


class SQLCourseResponse(SQLCourseCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


# ---------------- USER SCHEMAS ----------------

class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(
        min_length=8,
        max_length=72,
    )

    @field_validator("password")
    @classmethod
    def password_must_fit_bcrypt_bytes(cls, value: str) -> str:
        if len(value.encode("utf-8")) > 72:
            raise ValueError(
                "Password must not exceed 72 bytes in UTF-8 form"
            )
        return value


class UserResponse(UserBase):
    id: int
    created_at: datetime
    is_verified: bool

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
        frozen=True,
        validate_assignment=True,
        str_strip_whitespace=True,
    )


# ---------------- LOGIN SCHEMA ----------------

class UserLogin(UserBase):
    password: str


# Compatibility alias if your router uses LoginRequest
LoginRequest = UserLogin


# ---------------- FORGOT PASSWORD ----------------

class ForgotPasswordRequest(BaseModel):
    email: EmailStr


# ---------------- RESET PASSWORD ----------------

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(
        min_length=8,
        max_length=72,
    )

    @field_validator("new_password")
    @classmethod
    def password_must_fit_bcrypt_bytes(cls, value: str) -> str:
        if len(value.encode("utf-8")) > 72:
            raise ValueError(
                "Password must not exceed 72 bytes in UTF-8 form"
            )
        return value


# ---------------- JWT TOKEN SCHEMAS ----------------

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    id: Optional[int] = None


# Compatibility aliases for the router
TokenResponse = Token
UserOut = UserResponse
