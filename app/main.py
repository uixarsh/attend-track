from fastapi import FastAPI
from app.core.db import Base, engine
from app.core import models
from app.api.main import api_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Attendanace Management System")
app.include_router(api_router)