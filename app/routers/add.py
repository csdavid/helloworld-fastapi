from fastapi import FastAPI
from pydantic import BaseModel

router = APIRouter()


# Function with explicit typing
@router.get("/add/{a}/{b}")
def sum_values(a: int, b: int) -> dict:
    result = a + b
    return {"result": result}


# Creating a Basic Endpoint
@router.get("/add/")
def root():
    return {"message": "API working correctly!"}


# Defining Parameters in the URL
@router.get("/add/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}, welcome to FastAPI"}


# Query Parameters
@router.get("/add/sum")
def sum_query(a: int, b: int):
    return {"result": a + b}


class User(BaseModel):
    name: str
    age: int


# Use of HTTP Method POST
@router.post("/add/users/")
def create_user(user: User):
    return {"message": f"User {user.name} created successfully!"}
