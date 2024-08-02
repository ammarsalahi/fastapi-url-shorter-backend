from sqlalchemy import Column,String,Integer
from database import Base

class LinkModel(Base):
    __tablename__="links"

    id=Column(Integer,primary_key=True)
    url=Column(String)
    short_url=Column(String,unique=True)
    created_at=Column(String)

    