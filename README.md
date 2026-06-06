# 🎥 VideoMind AI

VideoMind AI is a Full-Stack AI-powered Video Intelligence Platform that enables users to upload videos or process YouTube links, generate transcripts, create AI-powered summaries, chat with video content, extract actionable insights, and manage video history through a secure authentication system.

---

## 🚀 Features

### 🔐 Authentication & Security

* User Signup & Login
* JWT Authentication
* Password Hashing using bcrypt
* Protected APIs
* User-specific data access

### 📤 Video Processing

* Upload Video/Audio Files
* Process YouTube Videos
* Audio Extraction & Conversion
* Fast Speech-to-Text Transcription using Faster-Whisper
* Hinglish Transcription using Sarvam AI

### 🤖 AI Features

* AI-Generated Video Summaries
* AI-Generated Titles
* Retrieval-Augmented Generation (RAG) Chat
* Ask Questions About Video Content
* Context-Aware Responses

### 🧠 Insight Extraction

* Action Items Extraction
* Key Decisions Extraction
* Unresolved Questions Extraction

### 💾 Persistence Layer

* PostgreSQL Database Integration
* Store Uploaded Videos
* Store Transcripts
* Store Summaries
* Store Chat History
* User-Specific Video Records

### 📂 Video History Management

* View Uploaded Videos
* View Previous Summaries
* View Previous Chat Sessions
* Delete Videos

### 📊 Dashboard Analytics

* Total Videos Uploaded
* Total Summaries Generated
* Total Questions Asked
* Total Chat Sessions
* Interactive Charts & Visualizations

---

## 🏗️ System Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
FastAPI Backend
  │
  ├── Authentication (JWT)
  ├── Video Processing
  ├── AI Services
  ├── RAG Chat
  ├── Dashboard Analytics
  │
  ▼
PostgreSQL Database

Videos
Transcripts
Summaries
Chats

  │
  ▼
ChromaDB Vector Store

  │
  ▼
Mistral AI + Faster Whisper + Sarvam AI
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* SQLAlchemy
* Pydantic

### Database

* PostgreSQL

### AI & NLP

* LangChain
* Mistral AI
* Faster-Whisper
* Sarvam AI

### Vector Database

* ChromaDB

### Authentication

* JWT
* OAuth2
* Passlib
* bcrypt

### Visualization

* Plotly
* Pandas

---

## 📁 Project Structure

```text
VideoMind-AI/

├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── pages/
│   ├── components/
│   ├── utils/
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/VideoMind-AI.git

cd VideoMind-AI
```

---

### Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Create `.env`

```env
MISTRAL_API_KEY=your_key

SARVAM_API_KEY=your_key

SARVAM_STT_MODEL=saaras:v2.5

WHISPER_MODEL=base

DATABASE_URL=postgresql://username:password@localhost/videomind_ai

JWT_SECRET_KEY=your_secret_key

JWT_ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Run Backend

```bash
uvicorn app.main:app --reload
```

---

### Frontend Setup

```bash
cd frontend

pip install -r requirements.txt
```

Run Frontend

```bash
streamlit run app.py
```

---

## 📖 API Endpoints

### Authentication

```http
POST /api/auth/signup

POST /api/auth/login

GET /api/auth/me
```

### Upload

```http
POST /api/upload

POST /api/youtube
```

### Summary

```http
POST /api/summary

POST /api/title
```

### Chat

```http
POST /api/chat
```

### Extraction

```http
POST /api/extract/action-items

POST /api/extract/questions

POST /api/extract/decisions
```

### Video History

```http
GET /api/videos

GET /api/videos/{video_id}

GET /api/videos/{video_id}/chats

DELETE /api/videos/{video_id}
```

### Dashboard

```http
GET /api/dashboard
```

---

## 📈 Future Enhancements

* PDF Export
* Meeting Minutes Generation
* Multi-Video Chat
* Advanced Dashboard Analytics
* Docker Deployment
* Cloud Deployment
* Team Collaboration Features

---

## 👩‍💻 Author

**Aditi Nagave**

VideoMind AI was developed as a Full-Stack AI Video Intelligence Platform integrating Generative AI, Retrieval-Augmented Generation (RAG), Speech-to-Text, Authentication, and Data Analytics to transform video content into actionable insights.
