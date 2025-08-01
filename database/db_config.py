from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from utils.config import DB_DRIVER, DB_USER, DB_PASS, DB_HOST, DB_DATA

#configuracion de db
url = URL.create(
    DB_DRIVER,
    username=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    database=DB_DATA
)

#motor de bd
engine = create_engine(url)

#sesion de trabajo
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    return SessionLocal()