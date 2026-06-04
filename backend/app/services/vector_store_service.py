# backend/app/services/vector_store_service.py

from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from app.services.embedding_service import get_embeddings
from app.core.config import settings


def build_vector_store(
    transcript: str,
    video_id: int
):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(transcript)

    docs = [
        Document(
            page_content=chunk,
            metadata={
                "chunk_index": i,
                "video_id": video_id
            }
        )
        for i, chunk in enumerate(chunks)
    ]

    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        collection_name=f"video_{video_id}",
        persist_directory=settings.CHROMA_DIR
    )

    return vector_store


def load_vector_store(
    video_id: int
):

    embeddings = get_embeddings()

    return Chroma(
        collection_name=f"video_{video_id}",
        embedding_function=embeddings,
        persist_directory=settings.CHROMA_DIR
    )


def get_retriever(
    vector_store,
    k: int = 4
):

    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )