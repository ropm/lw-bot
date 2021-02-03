from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# using lightweight app, no db
from lightweight_api import routes


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://127.0.0.1:8000"
]

app.include_router(routes.router, prefix='/api')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
