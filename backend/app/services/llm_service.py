# backend/app/services/llm_service.py
from langchain_mistralai import ChatMistralAI
from app.core.config import settings

def get_mistral_llm(
    temperature: float = 0.3,
    model: str = "mistral-small-latest"
):
    return ChatMistralAI(
        model=model,
        mistral_api_key=settings.MISTRAL_API_KEY,
        temperature=temperature,
    )