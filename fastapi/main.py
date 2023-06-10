from fastapi import FastAPI
from enum import Enum

# initiate app 
app = FastAPI()

# set up GET route 
@app.get('/', description="This is the main description for the root route")
# you can run this with uvicorn main:app --port=8000 --reload
async def root():
    return {"message": "hello test"}

# set up post route
@app.post("/")
async def post():
    return {"message": "hello from the post route"}

@app.put("/")
async def put():
    return {"message": "hello from the put route"}

### INTRODUCTION TO PATH PARAMETERS

# @app.get("/items/{item_id}")
# async def get_item(item_id):
#     return {"item_id": item_id}


# Enum class
class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

# get request for specific food with {food_name} parameter
@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
		# checks to see if food_name is vegetable
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}

		# check if fruit
    if food_name == "fruits":
        return {
            "food_name": food_name,
            "message": "you are still healthy, but like sweet things"
        }

		# it will be a dairy food
    return {"food_name": food_name, "message": "unlucky"}

### QUERY PARAMETERS

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]
