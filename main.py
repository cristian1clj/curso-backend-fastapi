# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path


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
    user_name: Optional[str] = Query(
        None, 
        min_length=3, 
        max_length=30, 
        title="User name", 
        description="This es the user name. Its between 3 and 30 characters"
        ), 
    mail: str = Query(
        ..., 
        min_length=8, 
        max_length=50, 
        title="User mail", 
        description="This is the user mail. Its required"
        )
):
    return {user_name: mail}


# Validation path paraeters
@app.get("/user/detail/{person_id}")
def show_user(
    person_id: int = Path(
        ..., 
        gt=0, 
        title="ID", 
        description="This is the user ID. Its required"
        )
):
    return {person_id: True}