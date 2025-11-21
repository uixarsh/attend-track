from fastapi import FastAPI
from database import Base, engine
from apis import router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Attendanace Management System")
app.include_router(router)



if "__main__" == __name__:
    import uvicorn 
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)