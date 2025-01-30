from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from sqlalchemy.exc import SQLAlchemyError

from database import get_db, engine, Base
from constant.constant import AppConstant
from model.user_model import CreateUser,UserTable
from model.register_model import Register,RegisterTable

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.post("/create_user") 
def create_user(create_user: CreateUser, db: Session = Depends(get_db)): 
    try:
        exist_email = db.query(UserTable).filter(UserTable.email == create_user.email).first()
        if exist_email:
            return AppConstant.getErrorModel(error="Email already registered")
        
        check_password = AppConstant.check_password_strength(create_user.password) 
        if(check_password !="Strong Password"):
            return AppConstant.getErrorModel(error=f"{str(check_password)}. Enter like this StrongPass123!")
     
        new_user = UserTable(name=create_user.name, email=create_user.email, password=AppConstant.check_password_strength(create_user.password)) 
        db.add(new_user)     
        db.commit()
        db.refresh(new_user) 
        return AppConstant.getSuccessModel(data=new_user)
    
    except Exception as e:
        db.rollback()
        return  AppConstant.getErrorModel(error=str(e))    
 
@app.get("/users")
def getUser(db: Session = Depends(get_db)): 
    try:
        get_user = db.execute(text("SELECT * FROM users")).fetchall()
        result =AppConstant.getSuccessModel(data=[dict(row._mapping) for row in get_user])
        return result
    
    except SQLAlchemyError as e:  
        db.rollback() 
        error_message = f"Database error: {str(e)}" 
        return AppConstant.getErrorModel(error=str(error_message))
     
    except Exception as e:   
        db.rollback()
        error_message = f"Unexpected error: {str(e)}"
        return AppConstant.getErrorModel(error=str(error_message))

@app.get("/expense_user")
def expenseUser(db: Session = Depends(get_db)):
    try:
        get_user = db.execute(text("SELECT * FROM expense_user")).fetchall()
        result =AppConstant.getSuccessModel(data=[dict(row._mapping) for row in get_user])
        return result
    
    except SQLAlchemyError as e:  
        db.rollback() 
        error_message = f"Database error: {str(e)}" 
        return AppConstant.getErrorModel(error=str(error_message))
     
    except Exception as e:   
        db.rollback()
        error_message = f"Unexpected error: {str(e)}"
        return AppConstant.getErrorModel(error=str(error_message))

# POST Method to Register a User
@app.post("/register")
def registerUser(register: Register, db: Session = Depends(get_db)):

    exist_email = db.query(RegisterTable).filter(RegisterTable.email == register.email).first()
    if exist_email:
        return AppConstant.getErrorModel(error="Email already registered")

    new_user = RegisterTable(  
        first_name=register.first_name,
        last_name=register.last_name, 
        email=register.email,
        password=register.password,
        profile_pic=register.profile_pic,
        id_token=register.id_token
    )
    
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return AppConstant.getSuccessModel(data=new_user) 
    
    except Exception as e:
        db.rollback() 
        return AppConstant.getErrorModel(error=f"Database error: {str(e)}")