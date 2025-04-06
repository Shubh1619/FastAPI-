from fastapi import FastAPI
from routers import items
from database import engine
from models import item

# Create database tables
item.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Item Storage API")

app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Item Storage API"}
