from fastapi import FastAPI
from .routes.product_routes import router as r
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# create a instance
app=FastAPI()

# allow CORS
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173"  # React (Vite)
]


# upload file se image frontend me load karne ke liya
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# allow operations
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
  return {"msg":"server is running"}

app.include_router(r)