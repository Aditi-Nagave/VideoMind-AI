# frontend/pages/Extraction.py
import streamlit as st

from utils.api import (
    extract_action_items,
    extract_questions,
    extract_decisions
)

st.title("🧠 AI Extraction")

if "transcript" not in st.session_state:

    st.warning(
        "Please upload/process a video first."
    )

else:

    transcript = st.session_state["transcript"]

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("Extract Action Items"):

            with st.spinner("Extracting Action Items..."):

                response = extract_action_items(
                    transcript
                )

                st.subheader("Action Items")

                st.write(response["action_items"])

    with col2:

        if st.button("Extract Questions"):

            with st.spinner("Extracting Questions..."):

                response = extract_questions(
                    transcript
                )

                st.subheader("Questions")

                st.write(response["questions"])

    with col3:

        if st.button("Extract Decisions"):

            with st.spinner("Extracting Decisions..."):

                response = extract_decisions(
                    transcript
                )

                st.subheader("Decisions")

                st.write(response["decisions"])