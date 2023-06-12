from curses import raw
from email.mime import base
from fastapi import FastAPI, Body, Path, Query
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl, EmailStr

# initiate app
app = FastAPI()

@app.get("/")
async def main():
    return {"message": "this is the root route"}

### Extra Models

class UserBase(BaseModel):
    username: str 
    email: EmailStr 
    full_name: Optional[str] = None 

class UserIn(UserBase):
    password: str 

class UserOut(BaseModel):
    pass

class UserInDB(UserBase):
    hashed_password: str 

def fake_password_hasher(raw_password: str):
    return f"supsersecret {raw_password}"

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    return user_in_db

@app.post("/user", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved