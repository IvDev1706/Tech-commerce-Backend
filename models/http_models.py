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