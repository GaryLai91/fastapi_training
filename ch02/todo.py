from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

todo_list = []

class Todo(BaseModel):
    id: int
    item: str

class TodoItem(BaseModel):
    item: str


@router.post("/todo")
async def add_todo(todo: Todo):
    todo_list.append(todo)
    return {
        'message': 'Todo added successfully'
    }

@router.get("/todo")
async def retrieve_todo():
    return {
        'todos': todo_list
    }

@router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }    
        
    return {"message": "To do with supplied id doesn't exist"}

@router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "todo": todo
            }
    return {"message": "To do with supplied id doesn't exist"}

@router.get("/hello")
async def say_hello() -> dict:
    return {"message": "Hello!"}


@router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully."
                }
    return {
        "message": "Todo with supplied ID doesn't exist."
    }


@router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todos deleted successfully."
    }
