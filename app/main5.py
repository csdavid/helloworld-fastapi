from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class PartialProduct(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None


class Product(BaseModel):
    name: str
    price: float


@app.get("/products")
def list_products():
    return [
        {"id": 1, "name": "Laptop", "price": 10.0},
        {"id": 2, "name": "Smartphone", "price": 20.0},
    ]


@app.post("/products")
def create_product(product: Product):
    return {"message": f"Product {product.name} successfully created"}


@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    return {"message": f"Product {product_id} updated to {product.name}"}


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    return {"message": f"Product {product_id} removed"}


@app.patch("/products/{product_id}")
def partially_update_product(product_id: int, product: PartialProduct):
    return {"message": f"Product {product_id} partially updated"}
