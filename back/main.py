from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session

DATABASE_URL = "sqlite:///./products.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class ProductModel(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)

Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()
    if not db.query(ProductModel).first():
        db.add_all([
            ProductModel(name="product1", price=12.50),
            ProductModel(name="Product2", price=100.00)
        ])
        db.commit()
    db.close()

seed()

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods= ["*"], allow_headers=["*"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Product(BaseModel):
    id: int
    name: str
    price: float

products = [
    Product(id=1, name="product1", price=12.50),
    Product(id=2, name="product2", price=10.00)
]

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(ProductModel).all()

from main import SessionLocal, ProductModel

db = SessionLocal()

p = db.query(ProductModel).filter(ProductModel.id == 2).first()
p.name = "Product2"
p.price = 100.00
db.commit()
db.close()