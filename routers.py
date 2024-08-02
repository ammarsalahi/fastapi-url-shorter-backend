from fastapi import APIRouter,Depends,Body
from typing import List,Annotated
from sqlalchemy.orm import Session
from schemas import Link,LinkCreate
from database import get_db
from operations import LinkOperation



router=APIRouter()

db_session=Annotated[Session,Depends(get_db)]


@router.get('/',response_model=List[Link])
async def list_link(db:db_session,offset:int=0,limit:int=100):
    return LinkOperation(db).list(offset,limit)

@router.post('/',response_model=Link)
async def create(db:db_session,data:LinkCreate=Body()):
    return LinkOperation(db).create(url=data.url)

@router.get('/{short_url}',response_model=Link)
async def get_link(db:db_session,short_url:str):
    return LinkOperation(db).get_link(short_url)

@router.delete('/{id}')
async def delete_link(db:db_session,id:int):
    return LinkOperation(db).delete(id)

