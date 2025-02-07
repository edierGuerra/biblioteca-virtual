from fastapi import APIRouter, Depends,Form,HTTPException
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session 
from database.utils import get_db
from security.tokens import create_token
from services.users_services import create_user,validate_email,validate_user

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
            raise HTTPException(401,detail="El correo ya se encuentra registrado")
        elif user_valid == False:
            user_data = create_user(
                user_name=name,
                user_email=email,
                user_password=password,
                db=db
            )
            return RedirectResponse("/user/login",status_code=303)
    except HTTPException as e: 
        raise e
    except Exception as ex:
        raise HTTPException(505,detail="Error inesperado")


@route.get("/logout",response_class=HTMLResponse)
def render_logout(request:Request):
    """
    # Formulario de registro usuario
    Carga el formulario de html para que el usuario puede ingresar sus datos
    """
    return template.TemplateResponse("pages/user_logout.html",{"request":request})

@route.post("/login/",response_class=RedirectResponse)
def login_user(email:str = Form(...),password:str = Form(...),db:Session = Depends(get_db),status_login:bool = False):
    valide = validate_user(email,password,db)
    if valide:
        access_token = create_token(data={"sub":email},expires_delta=30)
        return RedirectResponse(url=f"/home?token={access_token}",status_code=303)
    raise HTTPException(401,detail="Usuario o contraseña incorrectos.")

@route.get("/login",response_class=HTMLResponse)
def render_login(request:Request):
    return template.TemplateResponse("pages/user_login.html",{"request":request})