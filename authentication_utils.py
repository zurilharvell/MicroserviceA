#This will be updated!
#Zuri LH

import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
import os

password_contxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

#ensures that the SECRET_KEY is securely stored & not hardcoded
SECRET_KEY = os.getenv("SECRET_KEY", "your_default_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verifyPassword(plain_pass, hashed_pass): -> bool:
    return password_contxt.verify(plain_passw, hashed_pass)

def get_password_hash(hashed_pass): -> str:
    return password_contxt.hash(hashed_pass)

def create_access_token(data: Dict[str, Any]): -> str:
    to_encode_data = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode_data.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode_data, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def decode_access_token(access_token: str): -> Optional[Dict[str, Any]]:
    try:
        decoding_payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoding_payload
    except jwt.PyJWTError:
        return None
