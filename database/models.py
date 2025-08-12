from sqlalchemy import MetaData, Table, Column, Integer, String, Float, DATE, ForeignKey

#objeto de metadata
metadata = MetaData()

#tablas
product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(20), nullable=False),
    Column("desc", String, default="Sin descripcion"),
    Column("units", Integer, default=0),
    Column("price",Float, default=0.0)
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(15), nullable=False, unique=True),
    Column("email", String, nullable=False),
    Column("password", String, nullable=False),
    Column("role", String(6), default="client")
)

order = Table(
    "order",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("date", DATE, nullable=False),
    Column("status", String(15), nullable=False),
    Column("amount", Float, default=0.0),
    Column("user", Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
)

productList = Table(
    "product_list",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("order", Integer, ForeignKey("order.id", ondelete="CASCADE"), nullable=False),
    Column("product", Integer, ForeignKey("product.id", ondelete="CASCADE"), nullable=False),
    Column("units", Integer, default=0)
)