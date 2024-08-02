from pydantic import BaseModel


class LinkBase(BaseModel):
    id:int
    url:str
    short_url:str
    created_at:str


class LinkCreate(BaseModel):
    url:str


class Link(LinkBase):
    id:int 

    class Config:
        orm_mode=True    