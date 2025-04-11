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


products = [
    {"id": 1, "name": "Laptop", "price": 10.0},
    {"id": 2, "name": "Smartphone", "price": 20.0},
]


@app.post("/products")
def create_product(product: Product):
    new_id = len(products) + 1
    new_product = {"id": new_id, **product.model_dump()}
    products.append(new_product)
    return new_product


@app.get("/products")
def list_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {"error": "Product not found"}


@app.put("/products/{product_id}")
def update_product(product_id: int, new_product: Product):
    for product in products:
        if product["id"] == product_id:
            product.update(new_product.model_dump())
            return product

    return {"error": "Product not found"}


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    global products
    products_length_before = len(products)
    products = [p for p in products if p["id"] != product_id]
    products_length_after = len(products)
    if products_length_before == products_length_after:
        return {"error": "Product not found"}
    else:
        return {"message": "Product removed"}
