from fastapi import FastAPI

app=FastAPI()

#users route
@app.get("/users/{user_id}")
def get_user(user_id:int,user_name:str):
    return {"user_id":user_id,
            "user_name":user_name}

#34:17