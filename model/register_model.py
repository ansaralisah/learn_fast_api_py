from pydantic import BaseModel

from sqlalchemy import Column, Integer, String, Text
from database import Base


class RegisterTable(Base):
    __tablename__ = 'expense_user'
 
    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    profile_pic = Column(Text, nullable=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    id_token = Column(Text, nullable=True)



class Register(BaseModel):
    first_name: str
    last_name: str
    profile_pic: str = None
    email: str
    password: str 
    id_token: str = None
