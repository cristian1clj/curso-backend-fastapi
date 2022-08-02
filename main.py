# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query


app = FastAPI()

# Models
class User(BaseModel):
    user_name: str
    mail: str
    first_name: str
    last_name: str
    age: Optional[int] = None


@app.get("/")
def home():
    return {"Hello": "world"}


# Request and response body
@app.post("/user/new")
def create_user(user: User = Body(...)):
    return user

# Validation query
@app.get("/user/detail")
def show_user(
    user_name: Optional[str] = Query(None, min_length=3, max_length=30), 
    mail: Optional[str] = Query(..., min_length=8, max_length=50)
):
    return {user_name: mail}