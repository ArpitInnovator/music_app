from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = "" 
    KEY: str = ""  
    CLOUDINARY_API_KEY: str = ""   