from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

from app.services.vector_store_service import (
    build_vector_store,
    get_retriever,
)

from app.services.llm_service import get_mistral_llm


def format_docs(docs):

    return "\n\n".join([
        doc.page_content for doc in docs
    ])


def build_rag_chain(transcript: str):

    vector_store = build_vector_store(transcript)

    retriever = get_retriever(vector_store)

    llm = get_mistral_llm()

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
Answer ONLY from transcript context.

Context:
{context}
"""
        ),
        ("human", "{question}")
    ])

    rag_chain = (
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain


def ask_question(rag_chain, question: str):

    return rag_chain.invoke(question)