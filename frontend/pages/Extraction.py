import streamlit as st

from utils.api import (
    extract_action_items,
    extract_questions,
    extract_decisions
)

# =========================
# LOGIN REQUIRED
# =========================

if "token" not in st.session_state:

    st.warning(
        "Please login first."
    )

    st.stop()

st.title("🧠 AI Extraction")

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

    token = st.session_state[
        "token"
    ]

    col1, col2, col3 = st.columns(3)

    # =========================
    # ACTION ITEMS
    # =========================

    with col1:

        if st.button(
            "Extract Action Items"
        ):

            with st.spinner(
                "Extracting Action Items..."
            ):

                response = extract_action_items(
                    video_id,
                    transcript,
                    token
                )

                st.subheader(
                    "Action Items"
                )

                st.write(
                    response.get(
                        "action_items",
                        "No action items found"
                    )
                )

    # =========================
    # QUESTIONS
    # =========================

    with col2:

        if st.button(
            "Extract Questions"
        ):

            with st.spinner(
                "Extracting Questions..."
            ):

                response = extract_questions(
                    video_id,
                    transcript,
                    token
                )

                st.subheader(
                    "Questions"
                )

                st.write(
                    response.get(
                        "questions",
                        "No questions found"
                    )
                )

    # =========================
    # DECISIONS
    # =========================

    with col3:

        if st.button(
            "Extract Decisions"
        ):

            with st.spinner(
                "Extracting Decisions..."
            ):

                response = extract_decisions(
                    video_id,
                    transcript,
                    token
                )

                st.subheader(
                    "Decisions"
                )

                st.write(
                    response.get(
                        "decisions",
                        "No decisions found"
                    )
                )