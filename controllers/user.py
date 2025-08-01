from fastapi import APIRouter, HTTPException, Path, Depends, Form
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.http_models import User, UserCreate
from utils.token import encode_token, decode_token
from database.models import user
from database.transactions import get, create
from typing import Annotated

#router de usuarios
router = APIRouter(prefix="/users", tags=["Users"])

#objeto de oauth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def decode_tk(tk: Annotated[str,Depends(oauth2_scheme)])->dict:
    return decode_token(tk)

#metodos REST
@router.get("/profile")
def get_info(recovered: Annotated[dict, Depends(decode_tk)])->JSONResponse:
    return JSONResponse(status_code=200, content=recovered)


@router.post("/create")
def create_user(usr:UserCreate)->JSONResponse:
    #pasar a la bd
    created = create(user,usr.model_dump())
    #verificar exito
    if not created:
        raise HTTPException(status_code=501, detail="usuario no creado")
    return JSONResponse(status_code=201, content={"created":True, "msg": "el usuario se ha credo"})

@router.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()])->JSONResponse:
    #buscar en la base de datos
    usr = get(user, "name", form_data.username)
    #verificar exito
    if not usr:
        raise HTTPException(status_code=404, detail="usuario inexistente")
    #generar token
    token = encode_token({"username":usr['name'], "email":usr['email']})
    #regresar datos (de momento)
    return JSONResponse(status_code=208, content={"logged":True, "access_token": token})