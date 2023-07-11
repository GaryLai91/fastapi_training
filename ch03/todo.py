from fastapi import APIRouter, HTTPException, status
from model import TodoItems



todo_router = APIRouter()
todo_list = [
    {"id": 0, "item": "item 1"},
    {"id": 1, "item": "item 2"}
]

@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }

@todo_router.get("/todo/{id}")
async def get_single_todo(todo_id: int) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )