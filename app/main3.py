from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()


class User(BaseModel):
    name: str = Field(..., min_lenght=3, max_length=50)
    age: int = Field(..., gt=0, lt=120)
    email: EmailStr


@app.post("/users")
def create_user(user: User):
    return {"message": f"User {user.name} successfully created"}
