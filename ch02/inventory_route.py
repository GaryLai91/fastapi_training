from fastapi import APIRouter
from pydantic import BaseModel
import sqlite3

inv_router = APIRouter()
# C:\\Users\\TMY-01\\Desktop\\fastapi_training\\ch02'
path = "inventory.db"
conn = sqlite3.connect(path,check_same_thread=False)
cur = conn.cursor()

class Item(BaseModel):
    name: str
    price: float

@inv_router.get("/inv")
def get_all():
    sql = "SELECT * FROM items"
    items = cur.execute(sql)
    return list(items)

@inv_router.get("/inv/{id}")
def get_single_inv(id:int):
    sql = f"SELECT * FROM items where id = {id}"
    item = cur.execute(sql)
    return list(item)

@inv_router.post("/inv")
def create_inv(item: Item):
    sql = "INSERT INTO items(name, price) VALUES (?, ?)"
    cur.execute(sql, (item.name, item.price))
    return {
        "message": "Item successfully inserted"
    }