from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()


class User(BaseModel):
    name: str
    password: str

    @field_validator("password")
    def validate_password(cls, v):
        print("Validating password")
        if not any(char in "!@#$%^&*()" for char in v):
            raise ValueError("The password must contain at least one special character")
        return v


@app.post("/users")
def create_user(user: User):
    return {"message": f"User {user.name} successfully created"}
