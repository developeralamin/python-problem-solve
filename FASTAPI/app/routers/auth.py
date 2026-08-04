
from fastapi import FastAPI,Request,HTTPException, Response,status,Depends,APIRouter
from passlib.context import CryptContext
from sqlalchemy.orm import Session, session
from .. database import engine, get_db
from .. import models, schemas
from .. import oauth2
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/login"
)

@router.post('/', status_code=status.HTTP_200_OK)
def login_user(user_credentails: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user_credentails.username).first()
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with email: {user_credentails.username} not found"
        )
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    if not password_context.verify(user_credentails.password, existing_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    access_token = oauth2.create_access_token(data={"user_id": existing_user.id})
    return {"access_token": access_token, "token_type": "bearer"}