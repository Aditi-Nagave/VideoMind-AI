# frontend/pages/Chat.py

import streamlit as st

from utils.api import (
    ask_chat,
    get_conversation_history
)

# =========================
# LOGIN REQUIRED
# =========================

if "token" not in st.session_state:

    st.switch_page(
        "pages/Login.py"
    )

# =========================
# PAGE TITLE
# =========================

st.title(
    "💬 Chat With Video"
)

# =========================
# VIDEO REQUIRED
# =========================

if (
    "transcript" not in st.session_state
    or
    "video_id" not in st.session_state
):

    st.warning(
        "Please upload/process a video first."
    )

    st.stop()

# =========================
# SESSION VARIABLES
# =========================

transcript = st.session_state[
    "transcript"
]

video_id = st.session_state[
    "video_id"
]

token = st.session_state[
    "token"
]

# =========================
# LOAD CHAT HISTORY
# =========================

if (
    "loaded_video_id" not in st.session_state
    or
    st.session_state["loaded_video_id"]
    != video_id
):

    history = get_conversation_history(
        video_id,
        token
    )

    messages = []

    for chat in history:

        messages.append(
            {
                "role": "user",
                "content": chat["question"]
            }
        )

        messages.append(
            {
                "role": "assistant",
                "content": chat["answer"]
            }
        )

    st.session_state[
        "messages"
    ] = messages

    st.session_state[
        "loaded_video_id"
    ] = video_id

# =========================
# DISPLAY CHAT HISTORY
# =========================

for message in st.session_state[
    "messages"
]:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )

# =========================
# CHAT INPUT
# =========================

prompt = st.chat_input(
    "Ask about this video..."
)

# =========================
# USER MESSAGE
# =========================

if prompt:

    # Show user message

    st.session_state[
        "messages"
    ].append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message(
        "user"
    ):

        st.write(
            prompt
        )

    # =========================
    # AI RESPONSE
    # =========================

    with st.chat_message(
        "assistant"
    ):

        with st.spinner(
            "Thinking..."
        ):

            response = ask_chat(
                video_id,
                transcript,
                prompt,
                token
            )

            answer = response.get(
                "answer",
                "Failed to generate answer."
            )

            st.write(
                answer
            )

    # =========================
    # SAVE TO SESSION MEMORY
    # =========================

    st.session_state[
        "messages"
    ].append(
        {
            "role": "assistant",
            "content": answer
        }
    )