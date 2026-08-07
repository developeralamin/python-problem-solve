#journey for databases
#User Request => Session Create => SQL Execute => Commit => Return Response => Session Close

from sqlalchemy import create_engine #connection with db
from sqlalchemy.ext.declarative import declarative_base  #base class inherit for models
from sqlalchemy.orm import sessionmaker #create session with db for work
from . config import settings


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL) #engine object to connect with database 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#explain autocommit = no database save automatically
# autoflush =send db query from Memory 
# bind=engine - this session will be work with database engine

Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:  # if the session close throw exception
        db.rollback()
        raise
    finally:
        db.close()

