#journey for databases
#User Request => Session Create => SQL Execute => Commit => Return Response => Session Close

from sqlalchemy import create_engine #connection with db
from sqlalchemy.ext.declarative import declarative_base  #base class inherit for models
from sqlalchemy.orm import sessionmaker #create session with db for work

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost/postgres" #database connection string

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
    finally:
        db.close()

