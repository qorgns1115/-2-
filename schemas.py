# schemas.py
from pydantic import BaseModel

class RegisterUser(BaseModel):
    username: str
    password: str
    appearance: str = "default"
    art_style: str = "default"

class LoginUser(BaseModel):
    username: str
    password: str

class DiaryEntry(BaseModel):
    user_id: int
    date: str
    content: str
