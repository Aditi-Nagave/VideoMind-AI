# backend/app/core/config.py
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

    SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")
    SARVAM_STT_MODEL = os.getenv("SARVAM_STT_MODEL", "saaras:v2.5")

    WHISPER_MODEL = os.getenv("WHISPER_MODEL", "small")

    CHROMA_DIR = "vector_db"
    COLLECTION_NAME = "meeting_transcript"
    DATABASE_URL = os.getenv("DATABASE_URL")

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
    LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")
    LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")



settings = Settings()