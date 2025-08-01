from sqlalchemy import MetaData, Table, Column, Integer, String, Float

#objeto de metadata
metadata = MetaData()

#tablas
product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement = True),
    Column("name", String(20), nullable=False),
    Column("desc", String, default="Sin descripcion"),
    Column("units", Integer, default=0),
    Column("price",Float, default=0.0)
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement = True),
    Column("name", String(15), nullable=False),
    Column("email", String, nullable=False),
    Column("password", String(10), nullable=False)
)