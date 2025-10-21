from fastapi import APIRouter
from app.api.auth.endpoints import login, logout, register 
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
from pydantic import BaseModel, EmailStr
from typing import Optional





router = APIRouter(
    prefix="/auth",
    tags=["auth"],

)
#dont know what im using hex 32?
SECRET_KEY = "d7f3c1b6e5274a8d9bd5804f75d4854edb752a52138c8b5d3b1a2e27e09ff484"
ALGORITHM = "HS256"
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    user_type: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class ForgotPassword(BaseModel):
    email: EmailStr

class ResetPassword(BaseModel):
    token: str
    new_password: str