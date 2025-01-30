from pydantic import BaseModel

class Register(BaseModel):
    first_name: str
    last_name: str
    profile_pic: str = None
    email: str 
    password: str  
    id_token: str = None 

class CreateUser(BaseModel):
    name: str
    email: str
    password: str  

    