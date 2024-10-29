# models.py
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    appearance: str = "default"
    art_style: str = "default"

class Diary(BaseModel):
    user_id: int
    date: str
    content: str
