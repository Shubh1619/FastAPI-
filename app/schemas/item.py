from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    email: str
    password: str

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        orm_mode = True