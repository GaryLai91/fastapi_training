from fastapi import FastAPI
from todo import todo_router
from inv_router import inv_router


main = FastAPI()
main.include_router(todo_router)
main.include_router(inv_router)