from sqlalchemy import TIMESTAMP, Column, Integer, String, Text, func
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

class UserTable(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
     