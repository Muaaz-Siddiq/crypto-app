from config import *
from pydantic import BaseModel, EmailStr, validator
import re

class SignupModel(BaseModel):
    fullname: str
    password: str
    email: EmailStr
    phone_no: str

    @validator("phone_no")
    def check_phoneNumber_format(cls, v):
        regExs = r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$"
        if not re.fullmatch(regExs, v):
            raise ValueError("Invalid Phone Number")
        return v

# print(SignupModel(fullname='asas',password='asassa',email='sasassa', phone_no='asdasda'))