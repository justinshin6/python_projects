from fastapi import FastAPI, Body, Path, Query
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl, EmailStr

# initiate app
app = FastAPI()



class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

# this will be inside of our input schema
class UserIn(UserBase):
    password: str

# this will be inside of our output schema 
class UserOut(UserBase):
    pass


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user

class Item(BaseModel):
    name: str 
    description: Optional[str] = None
    price: float 
    tax: Optional[float] = None
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "the bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.7},

}

# this will exclude the unset fields inside of the class 
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id:str):
    return items[item_id]

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item