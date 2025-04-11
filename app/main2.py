from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4


class UserInput(BaseModel):
    name: str
    age: int
    email: str


class UserOutput(BaseModel):
    id: str
    name: str
    age: int
    email: str


app = FastAPI()


@app.post("/users", response_model=UserOutput)
def create_user(user: UserInput):
    return UserOutput(id=str(uuid4()), **user.dict())
