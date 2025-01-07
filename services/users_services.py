from database.models.user import UserModel
from security.password_user import hash_password,validate_password
from sqlalchemy.orm import Session

#Crea un usuario en la base de datos
def create_user(db:Session,user_name:str,user_password:str,user_email:str)-> dict:
    try:
        user = UserModel(
            name = user_name,
            email = user_email
        )
        hashed_password = hash_password(user_password)
        user.password = hashed_password
        db.add(user)
        db.commit()
        db.refresh(user)
        return {
            "name":user.name,
            "email":user.email,
            "books":user.books
            }
    except Exception as e:
        print("Error inesperado: ",e)

#Valida que el usuario si exista
def validate_user(email:str,password:str,db:Session)-> bool:
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if user:
        hashed_password = user.password
        return validate_password(password,hashed_password)

# Valida si el corre esta registrado
def validate_email(email:str,db:Session):
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if user: 
        return True
    else:
        return False