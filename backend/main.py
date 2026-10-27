from fastapi import FastAPI
from database import SessionLocal
from sqlalchemy import text

app = FastAPI() 

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    with SessionLocal() as session:
        session.execute(text("SELECT 1"))
    return {"db": "ok"}