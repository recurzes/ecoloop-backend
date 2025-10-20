from fastapi import APIRouter
from app.api.auth.endpoints import login, logout, register 
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
from pydantic import BaseModel





router = APIRouter(
    prefix="/auth",
    tags=["auth"],

)
#dont know what im using hex 32?
SECRET_KEY = "d7f3c1b6e5274a8d9bd5804f75d4854edb752a52138c8b5d3b1a2e27e09ff484"
ALGORITHM = "HS256"
bycrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str