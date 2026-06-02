# app/api/routes/upload.py
from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os

from app.services.audio_service import process_input
from app.services.transcription_service import transcribe_all

router = APIRouter(prefix="/api", tags=["Upload"])

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    language: str = "english"
):

    try:
        file_path = os.path.join(
            UPLOAD_DIR,
            file.filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        chunks = process_input(file_path)

        transcript = transcribe_all(
            chunks,
            language=language
        )

        return {
            "message": "File uploaded successfully",
            "filename": file.filename,
            "transcript": transcript
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/youtube")
async def upload_youtube(
    youtube_url: str,
    language: str = "english"
):

    try:

        chunks = process_input(youtube_url)

        transcript = transcribe_all(
            chunks,
            language=language
        )

        return {
            "message": "YouTube video processed successfully",
            "youtube_url": youtube_url,
            "transcript": transcript
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

