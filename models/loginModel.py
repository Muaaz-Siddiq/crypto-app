from config import *
from pydantic import BaseModel, EmailStr, validator


class loginModel(BaseModel):
    email: EmailStr
    password: str