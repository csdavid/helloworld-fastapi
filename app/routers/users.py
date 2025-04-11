from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    name: str
    age: int
    email: str


@router.get("/users")
def list_users():
    return [
        {"id": 1, "name": "John", "email": ""},
        {"id": 2, "name": "David", "email": ""},
    ]


@router.post("/users")
def create_user(user: User):
    return {"message": f"User {user.name} successfully created"}
