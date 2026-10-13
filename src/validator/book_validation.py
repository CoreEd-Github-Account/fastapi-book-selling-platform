from typing import Optional

from sqlmodel import  Field, SQLModel



class CreateBookRequest(SQLModel):
    title: str 
    author: str
    price: int
    is_sold: bool 
    user_id: int
