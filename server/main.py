from fastapi import FastAPI #type:ignore
from models.base import Base
from routes import auth , song
from database import engine
from fastapi.middleware.cors import CORSMiddleware   #type:ignore

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return {'message': 'Welcome to Musical world'}
 
app.include_router(auth.router, prefix='/auth')
app.include_router(song.router, prefix='/song')

Base.metadata.create_all(engine)
