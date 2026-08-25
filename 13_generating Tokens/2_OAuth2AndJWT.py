from fastapi import FastAPI,HTTPException,Depends
from jose import jwt, JWTError
from datetime import datetime,timedelta, timezone
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext

app=FastAPI()

#JWT config
SECRET_KEY="mysecret"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

# password hashing setup
pwd_context=CryptContext(schemes=["pbkdf2_sha256"]) 

#OAuth setup
oauth2_schema=OAuth2PasswordBearer(tokenUrl="login")

# dummy user DB
fake_user_db={
    "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("1234")
    }
}

# hash passowrd
def hash_password(password:str):
    return pwd_context.hash(password)

#verify password
def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

#create token
def create_token(data:dict):
    to_encode=data.copy()
    expiry=datetime.now(timezone.utc)+timedelta(minutes=30)
    to_encode.update({
        "exp":expiry
    })
    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

#Login API(OAuth2 Form)
@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    user=fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password,user["hashed_password"]):
        raise HTTPException(
            status_code=400,
            detail="Invalid username or password"
        )
    access_token=create_token({"sub":form_data.username})

    return {
        "Access_token":access_token,
        "token_type":"bearer"
    }

#verify token
def verify_token(token:str=Depends(oauth2_schema)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username=payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

# protected route
@app.get("/protected")
def protected_route(username:str=Depends(verify_token)):
    return {
        "message":f"Hello {username}! you have accessed this proteced route"
    }