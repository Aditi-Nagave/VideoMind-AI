# frontend/pages/Summary.py
import streamlit as st

from utils.api import (
    get_video_details
)

if "token" not in st.session_state:

    st.switch_page(
        "pages/Login.py"
    )

if "video_id" not in st.session_state:

    st.warning(
        "No video selected."
    )

    st.stop()

video = get_video_details(
    st.session_state["video_id"],
    st.session_state["token"]
)

st.title(
    video["title"]
)

st.subheader(
    "Summary"
)

st.write(
    video["summary"]
)