from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

DATABASE_URL="sqlite:///./fast.db"

engine=create_engine(DATABASE_URL,connect_args={'check_same_thread':False})

SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base =declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()    
