import os
from jose import JWTError
from jose.jwt import decode,encode
from datetime import datetime, timedelta
SECRET_KEY = os.getenv('DB_PASSWORD') 
ALGORITHM = "HS256"

# Crear un token
def create_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# Decodifica el token validando si es correcto o no
def decode_access_token(token: str) -> dict:
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None