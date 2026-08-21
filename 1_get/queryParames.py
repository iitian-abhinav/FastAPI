from fastapi import FastAPI

app=FastAPI()

# its like abc?xyz
# the main thing we are looking for is this ?

#optional parameters
@app.get("/users")
def get_users(name:str=None):
    return {"Name":name}

# default parameters: /products?limit=200
@app.get("/products")
def get_products(limit: int=10):
    return {"limit":limit}

@app.get("/items")
def get_items(name:str=None, price:int=0):
    return  {
        "name":name,
        "price":price
    }