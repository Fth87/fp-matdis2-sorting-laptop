from fastapi import FastAPI
from api.routers import laptop_router

app = FastAPI()

app.include_router(laptop_router.router, prefix="/api/v1", tags=["laptops"])
