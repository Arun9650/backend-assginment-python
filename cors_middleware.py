from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def apply_cors_middleware(app: FastAPI):
    # Configure CORS settings
    origins = [
         "https://assgiemnt.vercel.app/",
         "http://localhost:3000",
         "http://localhost:3000/",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
