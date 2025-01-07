from fastapi import APIRouter, Depends,Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session 
from database.utils import get_db
from services.users_services import create_user,validate_email

route = APIRouter(prefix="/user")

template = Jinja2Templates("templates")

@route.post("/create/",response_class=RedirectResponse)
def create_users(
    name:str = Form(...),
    email:str = Form(...),
    password:str = Form(...),
    db:Session = Depends(get_db)
    ):
    """
    # Crear usuario
    crea un usuario en la base de datos.
    ## Argumentos:
    - name: Nombre del usuario.
    - email: Correo del usuario.
    - password: Contraseña del usuario.
    ## Retorna:
    Diccionario con los datos del usuario.
    """
    try:
        user_valid = validate_email(email,db)
        if user_valid == True:
            return {"message":"El correo ingresado ya se encuentra registrado"}
        elif user_valid == False:
            user_data = create_user(
                user_name=name,
                user_email=email,
                user_password=password,
                db=db
            )
            return RedirectResponse("/user/login",status_code=303)
        return {}
    except Exception as e: 
        print("A ocurrido un error inesperado: ", e)

@route.get("/logout",response_class=HTMLResponse)
def render_logout(request:Request):
    """
    # Formulario de registro usuario
    Carga el formulario de html para que el usuario puede ingresar sus datos
    """
    return template.TemplateResponse("pages/user_logout.html",{"request":request})