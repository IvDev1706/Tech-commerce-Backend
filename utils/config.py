import os
from dotenv import load_dotenv

#cargar los datos
load_dotenv()

#guardar variables
JWT_SECRET = os.environ.get("JWT_SECRET")
DB_DRIVER = os.environ.get("DB_DRIVER")
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_DATA = os.environ.get("DB_DATA")