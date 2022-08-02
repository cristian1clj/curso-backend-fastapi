# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body


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