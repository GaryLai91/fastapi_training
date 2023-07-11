from fastapi import FastAPI
from todo import todo_router


main = FastAPI()
main.include_router(todo_router)