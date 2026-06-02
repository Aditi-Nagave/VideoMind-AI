from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

from app.services.llm_service import get_mistral_llm


def build_chain(system_prompt: str):

    llm = get_mistral_llm(temperature=0.2)

    return (
        RunnablePassthrough()
        | RunnableLambda(lambda x: {"text": x})
        | ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{text}")
        ])
        | llm
        | StrOutputParser()
    )


def extract_action_items(transcript: str):

    chain = build_chain(
        "Extract action items with owner and deadline."
    )

    return chain.invoke(transcript)


def extract_key_decisions(transcript: str):

    chain = build_chain(
        "Extract key decisions from transcript."
    )

    return chain.invoke(transcript)


def extract_questions(transcript: str):

    chain = build_chain(
        "Extract unresolved questions from transcript."
    )

    return chain.invoke(transcript)