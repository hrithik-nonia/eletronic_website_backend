from fastapi import FastAPI
from .routes.product_routes import router as product_route
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .routes.job_portal_routes import router as job_portal_route

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

# product route include
app.include_router(product_route)

# job portel route include
app.include_router(job_portal_route)