from fastapi import FastAPI
from routers import users
from database import Base, engine

app = FastAPI(title="FastAPI Users API", version="1.0")

@app.get("/")
def read_root():
    return {"message": "API is working"}


Base.metadata.create_all(bind=engine)

app.include_router(users.router)
