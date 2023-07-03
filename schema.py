# build a schema using pydantic
from pydantic import BaseModel

class User(BaseModel):
    id: int | None
    email: str
    password: str
    is_active: bool | None

    class Config:
        orm_mode = True

class Item(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int

    class Config:
        orm_mode = True
        