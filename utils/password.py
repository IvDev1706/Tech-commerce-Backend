from passlib.context import CryptContext

#contexto de encriptado
pwd_context = CryptContext(schemes=["argon2"],deprecated="auto")

#funcion para hashear password
def hash_password(password: str)->str:
    return pwd_context.hash(password)

#funcion para verificar contraseña
def validate_password(plain_pass:str, hashed_pass:str)->bool:
    return pwd_context.verify(plain_pass, hashed_pass)