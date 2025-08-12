from fastapi import APIRouter, HTTPException, Depends, Header
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.http_models import User, UserCreate
from utils.token import encode_token, decode_token
from utils.password import hash_password, validate_password
from database.models import user
from database.transactions import get, create, modify
from typing import Annotated

#router de usuarios
router = APIRouter(prefix="/users", tags=["Users"])

#objeto de oauth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

#decodificador de token
def decode_tk(tk: Annotated[str,Depends(oauth2_scheme)])->dict:
    return decode_token(tk)

#dependencia de validar rol de header
def check_role(user_role: Annotated[str, Header()])->str:
    #validar el rol
    if user_role == "client":
        raise HTTPException(status_code=401, detail="el usuario no tiene el rol para")
    return user_role

#metodos REST
@router.get("/profile")
def get_info(recovered: Annotated[dict, Depends(decode_tk)])->User:
    usr = get(user,"name",recovered["username"])
    usr["password"] = "not showed"
    return User.model_validate(usr)


@router.post("/create")
def create_user(usr:UserCreate)->JSONResponse:
    #hashear contraseña
    usr.password = hash_password(usr.password)
    #pasar a la bd
    created = create(user,usr.model_dump())
    #verificar exito
    if not created:
        raise HTTPException(status_code=501, detail="usuario no creado")
    return JSONResponse(status_code=201, content={"created":True, "msg": "el usuario se ha credo"})

@router.put("/update")
def update_user(usr:User, data: Annotated[dict, Depends(decode_tk)])->JSONResponse:
    #hashear nueva contraseña
    usr.password = hash_password(usr.password)
    #pasar a la bd
    updated = modify(user,usr.model_dump())
    #verificar exito
    if not updated:
        raise HTTPException(status_code=501, detail="usuario no actualizado")
    return JSONResponse(status_code=201, content={"created":True, "msg": "el usuario se ha actualizado"})

@router.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()])->JSONResponse:
    #buscar en la base de datos
    usr = get(user, "name", form_data.username)
    #validar user name
    if not usr:
        raise HTTPException(status_code=404, detail="usuario incorrecto o inexsistente")
    #validar contraseña
    if not validate_password(form_data.password,usr.get("password")):
        raise HTTPException(status_code=400, detail="contraseña incorrecta")
    #generar token
    token = encode_token({"username":usr['name'], "email":usr['email']})
    #regresar datos (de momento)
    return JSONResponse(status_code=208, content={"user_id": usr.get("id"),"access_token": token})