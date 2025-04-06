from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(100), index=True)
    password = Column(String(100), index=True)
