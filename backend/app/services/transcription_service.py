# backend/app/services/transcription_service.py
from faster_whisper import WhisperModel
import requests
import os

from pydub import AudioSegment

from app.core.config import settings

_model = None

SARVAM_STT_TRANSLATE_URL = (
    "https://api.sarvam.ai/speech-to-text-translate"
)


def load_model():

    global _model

    if _model is None:

        _model = WhisperModel(
            settings.WHISPER_MODEL,
            device="cpu",
            compute_type="int8"
        )

    return _model


def transcribe_chunk_whisper(
    chunk_path: str
):

    model = load_model()

    segments, _ = model.transcribe(
        chunk_path,
        beam_size=1
    )

    return " ".join(
        segment.text
        for segment in segments
    )


def transcribe_chunk_sarvam(chunk_path: str):

    headers = {
        "api-subscription-key": settings.SARVAM_API_KEY
    }

    with open(chunk_path, "rb") as f:

        files = {
            "file": (
                os.path.basename(chunk_path),
                f,
                "audio/wav"
            )
        }

        data = {
            "model": settings.SARVAM_STT_MODEL
        }

        response = requests.post(
            SARVAM_STT_TRANSLATE_URL,
            headers=headers,
            files=files,
            data=data,
            timeout=120,
        )

    response.raise_for_status()

    return response.json().get("transcript", "")


def transcribe_all(chunks, language="english"):

    transcript = ""

    for chunk in chunks:

        if language == "hinglish":

            text = transcribe_chunk_sarvam(chunk)

        else:

            text = transcribe_chunk_whisper(chunk)

        transcript += text + " "

    return transcript.strip()