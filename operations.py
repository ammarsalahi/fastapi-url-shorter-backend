from sqlalchemy.orm import Session
from models import LinkModel
import random
import string
import jdatetime 
import datetime
from fastapi import HTTPException,status


class LinkOperation:

    def __init__(self,db_session) -> None:
        self.db_session=db_session

    def get_short_url(self):
        return ''.join(
            random.choices(
                string.ascii_letters+string.digits,k=8
            )
        )
    
    def get_datetime(self):
        fulltime=datetime.datetime.now()
        jalali_date=jdatetime.GregorianToJalali(gday=fulltime.day,gmonth=fulltime.month,gyear=fulltime.year)
        return '{}-{}-{} {}:{}'.format(
            jalali_date.jyear,jalali_date.jmonth,jalali_date.jday,fulltime.hour,fulltime.minute
        )

    def create(self,url:str):
        query=self.db_session.query(LinkModel).filter(LinkModel.url==url).first()
        if query is not None:
            return query
        link=LinkModel(
            url=url,
            short_url=self.get_short_url(),
            created_at=self.get_datetime()
        )    
        self.db_session.add(link)
        self.db_session.commit()
        self.db_session.refresh(link)
        return link
    
    def get_link(self,short_url:str):
        query=self.db_session.query(LinkModel).filter(LinkModel.short_url==short_url).first()
        if query is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="link not found!!!")
        return query
    
    def delete(self,id:int):
        query=self.db_session.query(LinkModel).filter(LinkModel.id==id).first()
        if query is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="link not found!!!")
        self.db_session.delete(query)
        self.db_session.commit()
        return {'message':'ok'}

    def list(self,offset:int,limit:int):
        return self.db_session.query(LinkModel).offset(offset).limit(limit).all()