from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from database.utils import get_db
from services.users_services import create_user

route = APIRouter(prefix="/user")

@route.post("/create/")
def create_users(name:str,email:str,password:str,db:Session = Depends(get_db)) -> dict:
    """
    # Crear usuario
    crea un usuario en la base de datos.
    ## Argumentos:
    - name: Nombre del usuario.
    - email: Correo del usuario.
    - password: Contraseña del usuario.
    ## Retorna:
    O con los datos del usuario.
    """
    try:
        user_data = create_user(
            user_name=name,
            user_email=email,
            user_password=password,
            db=db
        )
        return user_data
    except Exception as e: 
        print("A ocurrido un error inesperado: ", e)
    
