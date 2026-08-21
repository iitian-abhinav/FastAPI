from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

todos=[]

class ToDo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/todos")
def create_todo(todo:ToDo):
    todos.append(todo)
    return {
            "message":"TODO added",
            "data":todo
        }

#getting the entire data
@app.get("/todos")
def get_todos():
    return todos

#getting data only for a particular id
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return todo
    return {"error":"Todo not found"}

#updating data
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:ToDo):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[index]=updated_todo
            return {
                "message":"Data Updated",
                "data":updated_todo
            }
    return {"error":"data not found"}

#deleteing data
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos.pop(index)
            return {"message":"Data Deleted"}

#1:19:20