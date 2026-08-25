# for general data fetching in python
# import requests

# response=requests.get("https://jsonplaceholder.typicode.com/posts")
# data=response.json()
# print(data[:2])

from fastapi import FastAPI,HTTPException
import requests

app=FastAPI()

#get all data
@app.get("/posts")
def get_posts():
    url="https://jsonplaceholder.typicode.com/posts"
    response=requests.get(url)
    return response.json()

#get data as per user_id
@app.get("/posts/{post_id}")
def get_post(post_id:int):
    url="https://jsonplaceholder.typicode.com/posts/{post_id}"
    response=requests.get(url)
    if response.status_code!=200:
        raise HTTPException(
            status_code=404,
            detail="post id not found"
        )
    return response.json()

