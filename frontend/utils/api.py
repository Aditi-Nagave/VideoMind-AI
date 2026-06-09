# frontend/utils/api.py
import requests

BASE_URL = "http://127.0.0.1:8000/api"


def upload_file(
    file,
    token,
    language="english"
):

    files = {
        "file": file
    }

    params = {
        "language": language
    }

    headers = {
        "Authorization":
        f"Bearer {token}"
    }

    response = requests.post(
        f"{BASE_URL}/upload",
        files=files,
        params=params,
        headers=headers
    )

    return response.json()



def upload_youtube(
    youtube_url,
    token,
    language="english"
):

    params = {
        "youtube_url": youtube_url,
        "language": language
    }

    headers = {
        "Authorization":
        f"Bearer {token}"
    }

    response = requests.post(
        f"{BASE_URL}/youtube",
        params=params,
        headers=headers
    )

    return response.json()


# UPDATED

def generate_summary(
    video_id,
    transcript,
    token
):

    headers = {
        "Authorization":
        f"Bearer {token}"
    }

    response = requests.post(
        f"{BASE_URL}/summary",
        json={
            "video_id": video_id,
            "transcript": transcript
        },
        headers=headers
    )

    return response.json()


def generate_title(
    video_id,
    transcript,
    token
):

    headers = {
        "Authorization":
        f"Bearer {token}"
    }

    response = requests.post(
        f"{BASE_URL}/title",
        json={
            "video_id": video_id,
            "transcript": transcript
        },
        headers=headers
    )

    return response.json()


# UPDATED

def ask_chat(
    video_id,
    transcript,
    question,
    token
):

    headers = {
        "Authorization":
        f"Bearer {token}"
    }

    response = requests.post(
        f"{BASE_URL}/chat",
        json={
            "video_id": video_id,
            "transcript": transcript,
            "question": question
        },
        headers=headers
    )

    return response.json()


def extract_action_items(
    video_id,
    transcript,
    token
):

    headers = {
        "Authorization":
        f"Bearer {token}"
    }

    response = requests.post(
        f"{BASE_URL}/extract/action-items",
        json={
            "video_id": video_id,
            "transcript": transcript
        },
        headers=headers
    )

    return response.json()


def extract_questions(
    video_id,
    transcript,
    token
):

    headers = {
        "Authorization":
        f"Bearer {token}"
    }

    response = requests.post(
        f"{BASE_URL}/extract/questions",
        json={
            "video_id": video_id,
            "transcript": transcript
        },
        headers=headers
    )

    return response.json()


def extract_decisions(
    video_id,
    transcript,
    token
):

    headers = {
        "Authorization":
        f"Bearer {token}"
    }

    response = requests.post(
        f"{BASE_URL}/extract/decisions",
        json={
            "video_id": video_id,
            "transcript": transcript
        },
        headers=headers
    )

    return response.json()

def signup(
    name,
    email,
    password
):

    response = requests.post(
        f"{BASE_URL}/auth/signup",
        json={
            "name": name,
            "email": email,
            "password": password
        }
    )

    return response.json()

def login(
    email,
    password
):

    response = requests.post(
        f"{BASE_URL}/auth/login",
        data={
            "username": email,
            "password": password
        }
    )

    return response.json()

def get_user(token):

    response = requests.get(
        f"{BASE_URL}/auth/me",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    return response.json()

def get_video_history(token):

    response = requests.get(
        f"{BASE_URL}/videos",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    return response.json()


def get_video_details(
    video_id,
    token
):

    response = requests.get(
        f"{BASE_URL}/videos/{video_id}",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    return response.json()


def get_chat_history(
    video_id,
    token
):

    response = requests.get(
        f"{BASE_URL}/videos/{video_id}/chats",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    return response.json()


def delete_video(
    video_id,
    token
):

    response = requests.delete(
        f"{BASE_URL}/videos/{video_id}",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    return response.json()


def get_dashboard_stats(
    token
):

    response = requests.get(
        f"{BASE_URL}/dashboard",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    return response.json()


def get_conversation_history(
    video_id,
    token
):

    response = requests.get(
        f"{BASE_URL}/chat/history/{video_id}",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    return response.json()