import streamlit as st

from utils.api import ask_chat

st.title("💬 Chat With Video")

if "transcript" not in st.session_state:

    st.warning(
        "Please upload/process a video first."
    )

else:

    transcript = st.session_state["transcript"]

    question = st.text_input(
        "Ask Your Question"
    )

    if st.button("Ask AI"):

        with st.spinner("Generating Answer..."):

            response = ask_chat(
                transcript,
                question
            )

            st.subheader("Answer")

            st.write(response["answer"])