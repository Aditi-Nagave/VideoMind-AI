# frontend/pages/Chat.py
import streamlit as st

from utils.api import ask_chat

st.title("💬 Chat With Video")

if (
    "transcript" not in st.session_state
    or
    "video_id" not in st.session_state
):

    st.warning(
        "Please upload/process a video first."
    )

else:

    transcript = st.session_state[
        "transcript"
    ]

    video_id = st.session_state[
        "video_id"
    ]

    question = st.text_input(
        "Ask Question"
    )

    if st.button("Ask AI"):

        with st.spinner(
            "Generating Answer..."
        ):

            response = ask_chat(
                video_id,
                transcript,
                question
            )

            st.subheader("Answer")

            st.write(
                response["answer"]
            )

