from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name:str
    age:int

@app.post("/create-user")
def create_user(users:User):
    return {
        "message":"user created",
        "data":users
    }

#50:59