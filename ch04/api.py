from fastapi import FastAPI
from todo import todo_router
from fastapi.staticfiles import StaticFiles


main = FastAPI()
main.mount('/static', StaticFiles(directory='static'), name='static')
main.include_router(todo_router)