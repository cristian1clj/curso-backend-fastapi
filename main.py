# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path


app = FastAPI()

# Models
class Document_tipe(str, Enum):
    cc = "cc",
    ti = "ti"
    

class User(BaseModel):
    user_name: str = Field(
        ..., 
        min_length=3, 
        max_length=30
    )
    mail: EmailStr = Field(...)
    first_name: str = Field(
        ..., 
        min_length=3, 
        max_length=50
    )
    last_name: str = Field(
        ..., 
        min_length=3, 
        max_length=50
    )
    age: Optional[int] = Field(
        default=None, 
        gt=0, 
        le=100
    )
    document_tipe: Document_tipe = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "user_name": "losASRock", 
                "mail": "cristian1clj@gmail.com", 
                "first_name": "Cristian", 
                "last_name": "Losada", 
                "age": None, 
                "document_tipe": "cc"
            }
        }
    
class Location(BaseModel):
    city: str
    state: str
    country: str
    
    class Config:
        schema_extra = {
            "example":{
                "city": "La Ceja", 
                "state": "Antioquia", 
                "country": "Colombia"
            }
        }


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


# Validation request body
@app.put("/user/{user_id}")
def update_user(
    user_id: int = Path(
        ..., 
        gt=0, 
        title="ID", 
        description="This is the user ID."
    ), 
    user: User = Body(...), 
    location: Location = Body(...)
):
    results = user.dict()
    results.update(location.dict())
    
    return results