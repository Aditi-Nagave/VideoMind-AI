# 🎥 VideoMind AI

An AI-powered Video Intelligence Platform that transforms video/audio recordings into actionable insights using Speech-to-Text, Retrieval-Augmented Generation (RAG), Conversational AI, and Meeting Analytics.

Built with FastAPI, Streamlit, PostgreSQL, LangChain (LCEL), LangSmith, ChromaDB, Mistral AI, Faster-Whisper, Sarvam AI, JWT Authentication, and Conversational RAG.

---

## ⭐ Key Highlights

- Conversational RAG with Persistent Memory
- LangChain LCEL-based AI Pipelines
- LangSmith Observability & Tracing
- Faster-Whisper Speech-to-Text
- ChromaDB Semantic Search
- JWT Authentication & Protected APIs
- PostgreSQL-backed User History
- Real-Time ChatGPT-Style Interface
- Dashboard Analytics & Video Management

---

# 🚀 Features

## 🔐 Authentication & Authorization

- User Signup
- User Login
- JWT Authentication
- Password Hashing (bcrypt)
- Protected APIs
- User-Specific Data Access

---

## 🎙 Speech-to-Text Processing

- Upload Video/Audio Files
- YouTube Video Processing
- Faster-Whisper Transcription
- Sarvam AI Hinglish Support
- Automatic Audio Chunking

---

## 🧠 AI Summarization

- Meeting Summary Generation
- AI Title Generation
- Long Transcript Handling
- Map-Reduce Summarization Pipeline

---

## 💬 Conversational AI Chat

- Retrieval-Augmented Generation (RAG)
- Conversational RAG
- Persistent Chat Memory
- Context-Aware Follow-up Questions
- ChatGPT-Style Interface
- Video-Specific Conversations

---

## 📌 Meeting Intelligence

- Action Item Extraction
- Decision Extraction
- Question Extraction

---

## 📂 Video History Management

- View Uploaded Videos
- View Previous Summaries
- View Previous Chats
- Continue Conversations
- Delete Videos

---

## 📊 Dashboard Analytics

- Total Videos Uploaded
- Total Summaries Generated
- Total Questions Asked
- Total Chat Sessions
- Interactive Charts

---

### 🔍 LLM Observability & Monitoring

- LangSmith Tracing
- Prompt Monitoring
- RAG Pipeline Debugging
- Retrieval Inspection
- LLM Response Tracking
- Latency Monitoring

---

# 🏗️ System Architecture

```text
Video Upload / YouTube URL
            │
            ▼
      Audio Processing
            │
            ▼
     Faster-Whisper STT
            │
            ▼
        Transcript
            │
     ┌──────┴──────┐
     ▼             ▼
 Summarization     Embeddings
     │             │
     ▼             ▼
 Summary       ChromaDB
                     │
                     ▼
              Conversational
                   RAG
                     │
              ┌──────┴──────┐
              ▼             ▼
         Chat Memory    Retrieval
        (PostgreSQL)   Context
              │             │
              └──────┬──────┘
                     ▼
                     │
                     ▼
                  Mistral AI
                     │
                     ▼
                  LangSmith
              (Tracing & Monitoring)
                     │
                     ▼
                  Response
```

---

# 🛠️ Tech Stack

### Frontend

- Streamlit
- Plotly

### Backend

- FastAPI
- SQLAlchemy
- PostgreSQL

### AI / LLM

- LangChain
- LCEL (LangChain Expression Language)
- LangSmith
- ChromaDB
- Mistral AI
- Faster-Whisper
- Sarvam AI

### Authentication

- JWT
- OAuth2
- Passlib (bcrypt)

### Other Libraries

- Pydub
- yt-dlp
- python-dotenv

---

# 📁 Expanded Project Structure

```text
VideoMind-AI/
│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── auth.py
│   │   │       ├── upload.py
│   │   │       ├── summary.py
│   │   │       ├── chat.py
│   │   │       ├── extraction.py
│   │   │       ├── video.py
│   │   │       └── dashboard.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   └── security.py
│   │   │
│   │   ├── models/
│   │   │   ├── user_model.py
│   │   │   ├── video_model.py
│   │   │   ├── transcript_model.py
│   │   │   ├── summary_model.py
│   │   │   └── chat_model.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── auth_schema.py
│   │   │   ├── chat_schema.py
│   │   │   ├── summary_schema.py
│   │   │   └── video_schema.py
│   │   │
│   │   ├── services/
│   │   │   ├── auth_service.py
│   │   │   ├── user_service.py
│   │   │   ├── transcription_service.py
│   │   │   ├── audio_service.py
│   │   │   ├── youtube_service.py
│   │   │   ├── embedding_service.py
│   │   │   ├── vector_store_service.py
│   │   │   ├── rag_service.py
│   │   │   ├── llm_service.py
│   │   │   ├── summarization_service.py
│   │   │   ├── extraction_service.py
│   │   │   ├── transcript_service.py
│   │   │   ├── summary_db_service.py
│   │   │   ├── chat_db_service.py
│   │   │   ├── chat_memory_service.py
│   │   │   ├── dashboard_service.py
│   │   │   └── video_service.py
│   │   │
│   │   ├── utils/
│   │   │   ├── helpers.py
│   │   │   └── file_manager.py
│   │   │
│   │   └── main.py
│   │
│   ├── alembic/
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
│
├── frontend/
│   │
│   ├── pages/
│   │   ├── Home.py
│   │   ├── Login.py
│   │   ├── Signup.py
│   │   ├── Chat.py
│   │   ├── Summary.py
│   │   ├── Video_History.py
│   │   ├── Dashboard.py
│   │   └── Extraction.py
│   │
│   ├── components/
│   │   ├── sidebar.py
│   │   └── uploader.py
│   │
│   ├── utils/
│   │   └── api.py
│   │
│   ├── app.py
│   └── requirements.txt
│
├── uploads/
├── downloads/
├── vector_db/
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/VideoMind-AI.git

cd VideoMind-AI
```

---

## 2. Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## 3. Create Environment Variables

Create `.env`

```env
DATABASE_URL=postgresql://username:password@localhost/videomind

JWT_SECRET_KEY=your_secret_key

MISTRAL_API_KEY=your_mistral_key

SARVAM_API_KEY=your_sarvam_key

SARVAM_STT_MODEL=saaras:v2.5

WHISPER_MODEL=small

LANGCHAIN_API_KEY=your_langsmith_key

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=VideoMind-AI
```

---

## 4. Run Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

---

## 5. Run Frontend

```bash
cd frontend

pip install -r requirements.txt

streamlit run app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# 🧠 AI Features Implemented

### Retrieval-Augmented Generation (RAG)

- Transcript Chunking
- Embedding Generation
- ChromaDB Vector Storage
- Semantic Search
- Context-Aware Responses

### Conversational RAG

- Persistent Conversation Memory
- Follow-Up Question Understanding
- Chat History Injection into Prompt
- PostgreSQL-backed Memory

### Meeting Intelligence

- AI Summaries
- AI Titles
- Action Items
- Decisions
- Questions

### LangSmith Observability

- End-to-End RAG Tracing
- Prompt Inspection
- Retriever Monitoring
- LLM Response Tracking
- Latency Analysis
- Debugging and Evaluation of AI Workflows

### LangChain LCEL

- RunnablePassthrough
- RunnableLambda
- ChatPromptTemplate
- StrOutputParser
- Modular RAG Pipeline Composition
- Context Injection Workflows

---

# 📊 Dashboard Metrics

- Total Videos Uploaded
- Total Summaries Generated
- Total Questions Asked
- Total Chat Sessions

---

# 🔮 Future Enhancements

- Multi-Video RAG
- AI Meeting Minutes Generator
- Topic Detection
- Knowledge Graph Visualization
- Speaker Diarization
- PDF Export
- Email Sharing
- Docker Deployment
- Cloud Deployment

---

# 💼 Resume Description

### VideoMind AI – Conversational Video Intelligence Platform

- Built a full-stack AI platform for video/audio understanding using Faster-Whisper, Mistral AI, LangChain LCEL, and ChromaDB.
- Implemented Conversational RAG with persistent chat memory, semantic retrieval, AI summarization, and meeting intelligence extraction.
- Developed secure JWT-based authentication, user-specific history management, dashboard analytics, and real-time AI chat using FastAPI, PostgreSQL, and Streamlit.

---

# 👩‍💻 Author

**Aditi Nagave**

VideoMind AI – AI-Powered Video Understanding & Conversational Intelligence Platform 🚀