from fastapi import FastAPI

app=FastAPI()

# home route
@app.get("/")
def home():
    return {"message":"First GET API"}

#about route
@app.get("/about")
def about():
    return {"message":" this is about page"}

# users route
@app.get("/users")
def users():
    return {
        "users":["Abhinav","Matko"]
    }
