from pydantic import BaseModel, Field
from typing import List
from datetime import date
#modelos de datos http

#product para get y update
class Product(BaseModel):
    #campos
    id: int = Field(gt=0) #con field se agregan validaciones
    name: str = Field(max_length=20)
    desc: str
    units: int = Field(gt=0)
    price: float = Field(gt=0.0)

#product para create
class ProductCreate(BaseModel):
    name: str = Field(max_length=20)
    desc: str
    units: int = Field(gt=0)
    price: float = Field(gt=0.0)
    
#usuario para get y update
class User(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(max_length=15)
    email: str = Field(min_length=10)
    password: str = Field(min_length=5, max_length=10)
    role: str = Field(max_length=6)

#usuario para create
class UserCreate(BaseModel):
    name: str = Field(max_length=15)
    email: str = Field(min_length=10)
    password: str = Field(max_length=10)
    role: str = Field(max_length=6)

#producto de orden
class OrderProduct(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(max_length=20)
    units: int = Field(gt=0)
    price: float = Field(gt=0.0)

#producto de orden para create
class OrderProductCreate(BaseModel):
    id: int = Field(gt=0)
    units: int = Field(gt=0)

#orden para get y update
class Order(BaseModel):
    id: int = Field(gt=0)
    date: str | date
    status: str
    amount: float = Field(gt=0.0)
    user: int = Field(gt=0)
    
#orden para create
class OrderCreate(BaseModel):
    date: str
    status: str
    amount: float = Field(gt=0.0)
    user: int = Field(gt=0)
    products: List[OrderProductCreate]