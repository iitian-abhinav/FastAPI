from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name:str
    age:int
    password:str

# we are using this to send only some of the user data we wants to show in the frontend
# so now we will create a class UserResponse in which we will define the parameters that we wants to show to the user

class UserResponse(BaseModel):
    name:str
    age:int

@app.get("/user",response_model=UserResponse)     #response_model shows the output of response
def get_user():
    return {
        "name":"Abhinav",
        "age":22,
        "password":"123456"
    }