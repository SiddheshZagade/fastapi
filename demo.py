from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str]= None

@app.get("/")
def home():
    return{"Data":"Testing"} 

@app.get("/about")
def about():
    return {"Data":"About"} 

inventory = {
    1:{
        "name":"Milk",
        "price":3.99,
        "brand":"Regular"
    }
}    

@app.get("/get-item/{item_id}")
def get_item(item_id:int=Path(None,description="The ID of the item you'd like to view")):
    return inventory[item_id]

@app.post("/create-item/{item_id}")
def create_item(item_id:int,item:Item):
    if item_id in inventory: 
     return{"Error":"Item ID already exists"}

    inventory[item_id]={"name":item.name, "brand": item.brand,"price":item.price}
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id:int,item:Item):
    if item_id not in inventory: 
     return{"Error":"Item ID does not exists"}

    inventory[item_id].update={"name":item.name, "brand": item.brand,"price":item.price}
    return inventory[item_id]