# frontend/components/uploader.py
import streamlit as st

from utils.api import (
    upload_file,
    upload_youtube
)


def render_uploader():

    st.subheader("📤 Upload Video")

    language = st.selectbox(
        "Select Language",
        ["english", "hinglish"]
    )

    upload_option = st.radio(
        "Choose Input Type",
        ["Upload File", "YouTube URL"]
    )

    transcript = ""

    # ---------------- FILE UPLOAD ---------------- #

    if upload_option == "Upload File":

        uploaded_file = st.file_uploader(
            "Upload Video/Audio File",
            type=["mp3", "wav", "mp4"]
        )

        if uploaded_file:

            st.info(
                f"Selected File: {uploaded_file.name}"
            )

            if st.button("🚀 Process File"):

                with st.spinner(
                    "Processing File..."
                ):

                    response = upload_file(
                        uploaded_file,
                        language
                    )

                    transcript = response.get(
                        "transcript",
                        ""
                    )

                    st.session_state[
                        "transcript"
                    ] = transcript

                    st.success(
                        "Transcription Completed!"
                    )

    # ---------------- YOUTUBE ---------------- #

    else:

        youtube_url = st.text_input(
            "Enter YouTube URL"
        )

        if st.button("🚀 Process YouTube Video"):

            with st.spinner(
                "Processing YouTube Video..."
            ):

                response = upload_youtube(
                    youtube_url,
                    language
                )

                transcript = response.get(
                    "transcript",
                    ""
                )

                st.session_state[
                    "transcript"
                ] = transcript

                st.success(
                    "YouTube Processing Completed!"
                )

    # ---------------- TRANSCRIPT DISPLAY ---------------- #

    if "transcript" in st.session_state:

        st.subheader("📝 Transcript")

        st.text_area(
            "Transcript Output",
            st.session_state["transcript"],
            height=350
        )

