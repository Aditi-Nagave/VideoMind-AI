from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
    Depends
)
import traceback

from sqlalchemy.orm import Session

import shutil
import os

from app.core.database import get_db

from app.services.audio_service import process_input

from app.services.transcription_service import (
    transcribe_all
)

from app.services.video_service import (
    create_video
)

from app.services.transcript_service import (
    create_transcript
)

router = APIRouter(
    prefix="/api",
    tags=["Upload"]
)

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")
async def upload_file(

    file: UploadFile = File(...),

    language: str = "english",

    db: Session = Depends(get_db)
):

    try:

        file_path = os.path.join(
            UPLOAD_DIR,
            file.filename
        )

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        chunks = process_input(file_path)

        transcript = transcribe_all(
            chunks,
            language=language
        )

        # SAVE VIDEO

        video = create_video(
            db=db,
            title=file.filename,
            file_path=file_path
        )

        # SAVE TRANSCRIPT

        create_transcript(
            db=db,
            video_id=video.id,
            content=transcript
        )

        return {

            "message":
            "File uploaded successfully",

            "video_id": video.id,

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

    language: str = "english",

    db: Session = Depends(get_db)
):

    try:

        chunks = process_input(
            youtube_url
        )

        transcript = transcribe_all(
            chunks,
            language=language
        )

        # SAVE VIDEO

        video = create_video(
            db=db,
            title="YouTube Video",
            youtube_url=youtube_url
        )

        # SAVE TRANSCRIPT

        create_transcript(
            db=db,
            video_id=video.id,
            content=transcript
        )

        return {

            "message":
            "YouTube processed successfully",

            "video_id": video.id,

            "youtube_url": youtube_url,

            "transcript": transcript
        }

    except Exception as e:
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

