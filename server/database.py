import os
from sqlalchemy import create_engine
from dotenv import load_dotenv   #type: ignore
from sqlalchemy.orm import sessionmaker
from config import Settings

settings = Settings()

engine = create_engine(settings.DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()