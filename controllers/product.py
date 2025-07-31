from fastapi import APIRouter, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from models.http_models import Product, ProductCreate
from database.models import product
from database.transactions import getAll, get, getLike, create, modify, drop

#router de api
router = APIRouter(prefix="/products", tags=["Products"])

#rutas REST
@router.get("/")
def get_products()->List[Product]:
    data = getAll(product)
    return [Product.parse_obj(row) for row in data]

@router.get("/{id}")
def get_product(id: int = Path(gt=0))->Product:
    #buscar en bd
    data = get(product, id)
    #verifircar exito
    if not data:
        raise HTTPException(status_code=404, detail="producto no encontrado")
    #regresar los datos
    return Product.parse_obj(data)

@router.get("/with/")
def get_product_like(like:str = Query(min_length=3))->List[Product]:
    #buscar en bd
    data = getLike(product, like)
    return [Product.parse_obj(p) for p in data]

@router.post("/create")
def create_product(prod:ProductCreate)->JSONResponse:
    #añadir el producto
    created = create(product, prod.model_dump())
    #mandar error
    if not created:
        raise HTTPException(status_code=501, detail="producto no creado")
    #respuesta
    return JSONResponse(status_code=201, content={"created":True, "msg":"el producto se ha creado"})

@router.put("/update")
def update_product(prod:Product)->JSONResponse:
    #modificar en bd
    updated = modify(product,prod.model_dump())
    #verificar exito
    if not updated:
        raise HTTPException(status_code=502, detail="producto no actualizado")
    #respuesta
    return JSONResponse(status_code=202, content={"updated":True, "msg":"el producto se ha actualizado"})

@router.delete("/delete/{id}")
def delete_product(id:int = Path(gt=0))->JSONResponse:#con Path se validan parametros
    #eliminar de la bd
    deleted = drop(product,id)
    #verificar exito
    if not deleted:
        raise HTTPException(status_code=503, detail="producto no eliminado")
    #respuesta
    return JSONResponse(status_code=203, content={"deletec":True, "msg":"el producto se ha eliminado"})