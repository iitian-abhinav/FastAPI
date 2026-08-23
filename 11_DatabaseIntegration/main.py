import sqlite3  # for small projects
from fastapi import FastAPI,Depends

app=FastAPI()
conn=sqlite3.connect("test.db",check_same_thread=False)

cursor=conn.cursor()

cursor.execute("""
create table if not exists todos
(
id integer primary key,
title text,
completed text
)
""")

conn.commit()

@app.get("/")
def home():
    return {
        "message":"SQLite Connectef fine"
    }

#SQLAlchemy:- for enterprice perposes

from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base,Session

DATABASE_URL="sqlite:///./test.db"

engine=create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

sessionLocal=sessionmaker(bind=engine)

Base=declarative_base()

class Todo(Base):
    __tablename__="todos"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    completed=Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(db:Session=Depends(get_db)):
    return {
        "message":"DB connected fine"
    }