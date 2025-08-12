from fastapi import APIRouter, HTTPException, Path, Query, Depends
from fastapi.responses import JSONResponse
from .user import decode_tk
from models.http_models import OrderProduct, Order, OrderCreate
from database.models import product, productList, order
from database.transactions import getBy, create, drop, get, modify, getJoin
from typing import List, Annotated
#router de ordenes
router = APIRouter(prefix="/orders", tags=["Orders"])

#funciones REST
@router.get(path="/")
def get_order_by_user(data: Annotated[dict, Depends(decode_tk)], usr: int = Query(gt=0))->List[Order]:
    #obtener de la bd
    ords = getBy(order,"user",usr)
    return [Order.model_validate(row) for row in ords]

@router.get("/products/{id}")
def get_products_by_order(id:int, data: Annotated[dict, Depends(decode_tk)])->List[OrderProduct]:
    #obtener lso productos
    products = getJoin(productList.join(product, productList.c.product == product.c.id),productList.c.order,id)
    return [OrderProduct(id=prod["id"],name=prod["name"],units=prod["units"],price=prod["price"]) for prod in products]

@router.post(path="/create")
def create_order(ord: OrderCreate, data: Annotated[dict, Depends(decode_tk)])->JSONResponse:
    #crear orden
    created = create(order, {"date":ord.date,"status":ord.status,"amount":ord.amount,"user":ord.user})
    #verificar creacion
    if not created:
        raise HTTPException(status_code=500, detail="error al crear la orden")
    #guardar productos
    for prod in ord.products:
        dictP = prod.model_dump()
        if not create(productList, {"order":created,"product":dictP["id"],"units":dictP["units"]}):
            drop(order, created)
            raise HTTPException(status_code=500, detail="error al registrar producto")
        #actualizar productos
        prodO = get(product, "id", dictP["id"])
        prodO["units"] -= dictP["units"]
        modify(product, prodO)
    #respuesta al cliente
    return JSONResponse(status_code=201, content={"created":True, "msg": "orden creada!!!"})    