from fastapi import FastAPI,HTTPException,Depends,Header
from jose import jwt
from datetime import datetime,timedelta, timezone

app=FastAPI()

SECRET_KEY="mysecret"

ALGORITHM="HS256"

#creating token
def create_token(data:dict):
    to_encode=data.copy()
    expiry=datetime.now(timezone.utc)+timedelta(minutes=30)
    to_encode.update({
        "exp":expiry
    })
    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

# Login API(token generate)
@app.post("/login")
def login(username:str,password:str):
    if username!="admin" or password!="123":
        raise HTTPException(
            status_code=401,
            detail="Invalid username and password"
        )
    token=create_token({
        "sub":username
    })
    return {
        "access_token":token
    }

# token verification
def varify_token(token: str=Header(None)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

# protected route
@app.get("/secure")
def secure_data(user=Depends(varify_token)):
    return {
        "message":"Secure Data Accessed",
        "user":user
    }