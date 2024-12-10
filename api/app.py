from fastapi import FastAPI
from api.routers import laptop_router
from fastapi.middleware.cors import CORSMiddleware

# Inisialisasi aplikasi FastAPI
app = FastAPI(
    title="Laptop Filtering API",
    description="Upload file excel and filter and sort.",
)

# Konfigurasi middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tambahkan router
app.include_router(laptop_router.router, prefix="/api", tags=["Laptops"])


# Root endpoint
@app.get("/")
async def root():
    return {"message": "Laptop Filtering API is running!"}
