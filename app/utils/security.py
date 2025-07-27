from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi import HTTPException
from datetime import timedelta, datetime
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path(__file__).parents[1] / '.env'
load_dotenv(dotenv_path=dotenv_path)

SECRET_KEY = os.getenv("SECRETKEY")
ALGORITHM = "HS256"
TOKENEXPIRES =timedelta(minutes=30)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain: str):
	return pwd_context.hash(plain)

def verify_password(plain: str, hashed):
	return pwd_context.verify(plain, hashed)

def generate_token(data: dict, expire: timedelta = None):
	to_encode = data.copy()
	expire = datetime.utcnow() + (TOKENEXPIRES or expire)
	to_encode.update({'exp': expire})
	return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
	try:
		return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
	except JWTError:
		raise HTTPException(status_code=401, detail="Invalid Token")