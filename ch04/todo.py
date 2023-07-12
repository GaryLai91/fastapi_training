from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

todo_router = APIRouter()
todo_list = [
    {"title": "Hello World"},
    {"title": "hi"}
]

template = Jinja2Templates(directory="templates")

@todo_router.post("/todo")
def add_todo(request: Request):
    pass

@todo_router.get("/todo")
def add_todo(request: Request):
    return template.TemplateResponse('todo.html', {"request": request,"todos": todo_list})


@todo_router.get("/todo-create")
def create(request: Request):
    return template.TemplateResponse('todo-form.html', {"request": request})

@todo_router.post("/todo-save")
def save(request: Request, item:str = Form(...)):
    print('item =' + item)
    todo_list.append({"title": item})
    return "ok"