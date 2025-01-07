#from database.utils import create_db
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from routes.user_routes import route as user_router
from database.utils  import create_db 

templates = Jinja2Templates("templates") #Plantillas del proyecto

#Configura la api y su información
app = FastAPI(
    title="Sistema de biblioteca virtual",
    version="1.0",
    description="Le permite a los usuarios gestionar libros y descargarlos.",
    contact={"name":"Edier Andres Guerra Vargas","email":"edierguerra55@gmail.com"}
)

#Renderiza la pagina de index
@app.get("/",response_class=HTMLResponse,tags=["pages"],summary="Pagina de inicio",description="Renderiza la pagina que se le muestra a los usuario no registrados.")
async def index_page(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

#Renderiza la pagina principal 
@app.get("/home",tags=["pages"],response_class=HTMLResponse,summary="Pagina principal",description="Renderiza la pagina principal que se le muestra a los usuarios registrados.")
async def home_page(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})

# Rutas del proyecto
app.include_router(user_router)

