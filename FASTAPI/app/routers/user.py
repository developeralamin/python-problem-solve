
from fastapi import FastAPI,Request,HTTPException, Response,status,Depends,APIRouter
from passlib.context import CryptContext
from sqlalchemy.orm import Session, session
from .. database import engine, get_db
from typing import List, Optional
from .. import models, schemas

router = APIRouter(
    prefix="/sqlalchemy/users"
)

#user create
#user create

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate, db:Session = Depends(get_db)):
    new_user = models.User(**user.model_dump())
    exising_user = db.query(models.User).filter(models.User.email == user.email).first()
    if exising_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"User with email: {user.email} already exists"
        )
    hashed_password = CryptContext(schemes=["bcrypt"], deprecated="auto").hash(user.password)
    new_user.password = hashed_password
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


