from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def welcome():
    return "Hello World"

@app.get("/list")
async def list():
    return {
        "name": "gary"
    }