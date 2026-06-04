# frontend/utils/api.py
import requests

BASE_URL = "http://127.0.0.1:8000/api"


def upload_file(file, language="english"):

    files = {
        "file": file
    }

    params = {
        "language": language
    }

    response = requests.post(
        f"{BASE_URL}/upload",
        files=files,
        params=params
    )

    return response.json()


def upload_youtube(youtube_url, language="english"):

    params = {
        "youtube_url": youtube_url,
        "language": language
    }

    response = requests.post(
        f"{BASE_URL}/youtube",
        params=params
    )

    return response.json()


# UPDATED

def generate_summary(
    video_id,
    transcript
):

    response = requests.post(
        f"{BASE_URL}/summary",
        json={
            "video_id": video_id,
            "transcript": transcript
        }
    )

    return response.json()


def generate_title(transcript):

    response = requests.post(
        f"{BASE_URL}/title",
        json={
            "transcript": transcript
        }
    )

    return response.json()


# UPDATED

def ask_chat(
    video_id,
    transcript,
    question
):

    response = requests.post(
        f"{BASE_URL}/chat",
        json={
            "video_id": video_id,
            "transcript": transcript,
            "question": question
        }
    )

    return response.json()


def extract_action_items(transcript):

    response = requests.post(
        f"{BASE_URL}/extract/action-items",
        json={
            "transcript": transcript
        }
    )

    return response.json()


def extract_questions(transcript):

    response = requests.post(
        f"{BASE_URL}/extract/questions",
        json={
            "transcript": transcript
        }
    )

    return response.json()


def extract_decisions(transcript):

    response = requests.post(
        f"{BASE_URL}/extract/decisions",
        json={
            "transcript": transcript
        }
    )

    return response.json()
