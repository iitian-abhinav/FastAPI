# #######################"normal syntax"
# import time
# import asyncio

# async def task():
#     await asyncio.sleep(3)
#     return "Done"

###################### with FastAPI
# async meaning multiple requests are handled at the same time
import time
import asyncio
from fastapi import FastAPI

app=FastAPI()

@app.ger("/")
async def home():
    await asyncio.sleep(3)
    return {
        "message":"Async API"
    }