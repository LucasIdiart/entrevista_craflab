from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods= ["*"], allow_headers=["*"])

class Product(BaseModel):
    id: int
    name: str
    price: float

products = [
    Product(id=1, name="product1", price=12.50),
    Product(id=2, name="product2", price=10.00)
]

@app.get("/products")
def get_products():
    return products