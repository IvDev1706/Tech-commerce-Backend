from pydantic import BaseModel, Field

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
    password: str = Field(min_length=5, max_length=10, max_digits=5)
    
class UserCreate(BaseModel):
    name: str = Field(max_length=15)
    email: str = Field(min_length=10)
    password: str = Field(min_length=5, max_length=10)