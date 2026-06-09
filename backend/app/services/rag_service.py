# backend/app/services/rag_service.py
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

from app.services.vector_store_service import (
    build_vector_store,
    get_retriever,
)
from app.services.chat_memory_service import (
    format_chat_history
)

from app.services.llm_service import get_mistral_llm


def format_docs(docs):

    return "\n\n".join([
        doc.page_content for doc in docs
    ])


def build_rag_chain(
    transcript: str,
    video_id: int,
    history: str = ""
):

    vector_store = build_vector_store(
        transcript,
        video_id
    )

    retriever = get_retriever(
        vector_store
    )

    llm = get_mistral_llm()

    prompt = ChatPromptTemplate.from_messages([
        ( "system",
"""
You are an expert meeting assistant.

Use BOTH:

1. Chat History
2. Transcript Context

to answer.

Chat History:
{history}

Transcript Context:
{context}

Rules:

- Understand follow-up questions.
- Understand references such as:
  "that topic"
  "the second point"
  "tell me more"

- Use previous conversation.

- If answer is not found:
"I could not find this information in the meeting transcript."
"""
),
("human", "{question}")
])

    rag_chain = (
        {
             "context":
        retriever
        | RunnableLambda(format_docs),

    "history":
        RunnableLambda(
            lambda x: history
        ),

    "question":
        RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain


def ask_question(
    rag_chain,
    question: str
):

    return rag_chain.invoke(question)