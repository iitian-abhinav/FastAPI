from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app=FastAPI()

@app.post("/create_user",status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message":"User Created"
    }

@app.get("/user")
def get_user():
    return {
        "status":"Success",
        "message":"User Fetched",
        "data":{
            "user":"Abhinav",
            "age":22
        }
    }

#error handling
@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id!=1:
        raise HTTPException(
            status_code=404,
            detail="User not Found"
        )
    return {
        "status": "Success",
        "message": "User Found",
        "data": {
            "user": "Abhinav",
            "age": 22
        }
    }