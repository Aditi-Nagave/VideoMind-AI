# frontend/pages/Video_History.py
import streamlit as st

from utils.api import (
    get_video_history,
    get_video_details,
    get_chat_history,
    delete_video
)

if "token" not in st.session_state:

    st.switch_page(
        "pages/Login.py"
    )

st.title(
    "📂 My Videos"
)

# =========================
# DASHBOARD BUTTON
# =========================

if st.button(
    "📊 Open Dashboard"
):

    st.switch_page(
        "pages/Dashboard.py"
    )

videos = get_video_history(
    st.session_state["token"]
)

for video in videos:

    st.subheader(
        video["title"]
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            f"Summary {video['id']}"
        ):

            data = get_video_details(
                video["id"],
                st.session_state["token"]
            )

            st.session_state["video_id"] = data["id"]

            st.session_state["transcript"] = data["transcript"]

            st.session_state["saved_summary"] = data["summary"]

            st.switch_page(
                 "pages/Summary.py"
         )

    with col2:

        if st.button(
              f"Chats {video['id']}"
           ):

            data = get_video_details(
                video["id"],
                st.session_state["token"]
        )

            st.session_state["video_id"] = data["id"]

            st.session_state["transcript"] = data["transcript"]

            if "messages" in st.session_state:
                del st.session_state["messages"]

            if "loaded_video_id" in st.session_state:
                del st.session_state["loaded_video_id"]

            st.switch_page(
                  "pages/Chat.py"
               )

    with col3:

        if st.button(
            f"Delete {video['id']}"
        ):

            delete_video(
                video["id"],
                st.session_state["token"]
            )

            st.success(
                "Deleted"
            )

            st.rerun()