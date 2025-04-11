from fastapi import FastAPI
import app.routers.users as users
import app.routers.products as products

app = FastAPI()


@app.get("/")
def home():
    return {"message": "FastAPI server running!"}


app.include_router(users.router)
app.include_router(products.router)
