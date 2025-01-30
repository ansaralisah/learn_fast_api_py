from pydantic import BaseModel
from sqlalchemy import TIMESTAMP, Column, Integer, String, func
from database import Base

class CreateUser(BaseModel):
    name: str
    email: str
    password: str  

class UserTable(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
 