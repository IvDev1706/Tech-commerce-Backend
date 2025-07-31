from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

#configuracion de db
url = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="Isql1706",
    host="localhost",
    database="techcommerse"
)

#motor de bd
engine = create_engine(url)

#sesion de trabajo
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    return SessionLocal()