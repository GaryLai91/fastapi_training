from fastapi import FastAPI
from inventory_route import inv_router
from todo import router

main = FastAPI()
main.include_router(router)
main.include_router(inv_router)