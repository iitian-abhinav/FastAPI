from fastapi import FastAPI,Request
import time
app=FastAPI()

@app.middleware("http")
async def my_middleware(request:Request,call_next):
    print("Request")
    response=await call_next(request)
    print("Response sent")
    return response

# logging middleware(to know the time taken for the response by the API)
@app.middleware("http")
async def log_middleware(request:Request,call_next):
    start_time=time.time()
    response=await call_next(request)
    process_time=time.time()-start_time
    print(f"Path:{request.url.path} | Time:{process_time}")
    return response
