from fastapi import FastAPI
from api import router as api_router

app = FastAPI()

# Import and use the CORS middleware from cors_middleware.py
from cors_middleware import apply_cors_middleware
apply_cors_middleware(app)

# Mount the API router from api.py
app.include_router(api_router)
