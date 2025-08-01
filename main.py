#imports para la aplicacion de api
from fastapi import FastAPI
#necesarios para motor de plantillas
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
#middleware de cors
from fastapi.middleware.cors import CORSMiddleware
from controllers import product, user
#imports de bd
from database.models import metadata
from database.db_config import engine
import os

#instancia de app
app = FastAPI()

#middelware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#definir directorios
base_dir = os.path.dirname(__file__)
static_path = os.path.join(base_dir,'static')
templates_path = os.path.join(base_dir,'templates')

#montar los directorios (static y templates)
app.mount("/static",StaticFiles(directory=static_path),"static")
templates = Jinja2Templates(directory=templates_path)

#evento de inicio
@app.on_event("startup")
def startup():
    #crear las tablas en el engine
    metadata.create_all(engine)

#rutas
@app.get("/")
def home(request:Request):
    return templates.TemplateResponse('index.html',{'request':request, 'title':'Tech commerse backend'})

#añadir routers
app.include_router(user.router)
app.include_router(product.router)