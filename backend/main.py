from fastapi import FastAPI
from database import SessionLocal, Base, engine
from sqlalchemy import text
import models

app = FastAPI() 
Base.metadata.create_all(engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    with SessionLocal() as session:
        session.execute(text("SELECT 1"))
    return {"db": "ok"}