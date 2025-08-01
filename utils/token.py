from jose import jwt
from utils.config import JWT_SECRET

def encode_token(payload: dict)->str:
    return jwt.encode(payload,JWT_SECRET)

def decode_token(token: str)->dict:
    return jwt.decode(token,JWT_SECRET,"HS256")