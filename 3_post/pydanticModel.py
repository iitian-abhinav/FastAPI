from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import StrictInt

app=FastAPI()

# class User(BaseModel):
#     name:str
#     age:StrictInt
#     email:str

# @app.post("/create_user")
# def create_user(user:User):
#     return {
#         "message":"User Created",
#         "data":user
#     }

class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name:str
    age:StrictInt
    address: Address   #using another class as the variable

@app.post("/create-user")
def create_user(user:User):
    return {
        "data":user
    }