from pydantic import BaseModel
from typing import List

class TodoItem(BaseModel):
    item: str
    class Config:
        json_schema_extra = {
            "example": {
                "item": "The item name, i.e Shoe"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]
    class Config:
        json_schema_extra = {
            "example": {
                "todo": [
                    {"item": "Item 1"},
                    {"item": "Item 2"}
                ]
            }
        }