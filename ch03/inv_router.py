from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

# 1. create engine
# 2. session
# 3. execute
# 4. generate table using declarative_base from model
inv_router = APIRouter()

db_url = "sqlite:///./inventory.db"
engine = create_engine(db_url, connect_args={"check_same_thread":False})

Session = sessionmaker(bind=engine)
db = Session()

Base = declarative_base()
class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)  # primary key is unique and auto increment
    name = Column(String(100))
    price = Column(Float)

# Pydantic Item class
class PyItem(BaseModel):
    name: str
    price: float


# moment where a table is generated
Base.metadata.create_all(engine)

item = Item(name="shoes", price=9.99)
db.add(item) # this runs insert into (name, price) values('shoes', 9.99)



# list all the inventory
@inv_router.get('/inv')
async def get_all():
    rows = db.query(Item).all()
    db.close()
    return rows
    
# get one record of item
@inv_router.get("/inv/{id}")
async def get_single(id: int):
    item = db.query(Item).filter(Item.id == id).first()
    db.close()
    return item

@inv_router.post('/inv')
def create(pyitem: PyItem):
    item = Item(name=pyitem.name, price=pyitem.price)
    db.add(item)
    db.commit()
    db.refresh(item)
    db.close()
    return {
        "message": "ok"
    }
    

@inv_router.put("/inv/{id}")
def update(pyitem: PyItem, id: int):
    item = db.query(Item).filter(Item.id == id).first()
    item.name = pyitem.name
    item.price = pyitem.price
    db.commit()
    db.refresh(item)
    db.close()
    return item

@inv_router.delete("/inv/{id}")
def delete(id:int):
    item = db.query(Item).filter(Item.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="ID does not exist")
    db.delete(item)
    db.commit()
    db.close()
    return {
        "message": "ok"
    }