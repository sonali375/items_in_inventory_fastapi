from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
inventory_list = []


@app.get("/")
async def hello():
    return "welcome to application"


class Inventory(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price: int


@app.post("/add_product")
async def items(inventory: Inventory):
    inventory_list.append(inventory)
    return {"Inventory": inventory_list, "message": "welcome"}
