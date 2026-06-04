# frontend/pages/Home.py
import streamlit as st

from utils.api import (
    upload_file,
    upload_youtube,
    generate_summary,
    generate_title
)

st.title("📤 Upload & Summarize")

language = st.selectbox(
    "Select Language",
    ["english", "hinglish"]
)

upload_option = st.radio(
    "Choose Input Type",
    ["Upload File", "YouTube URL"]
)

transcript = ""

# ---------------- FILE ---------------- #

if upload_option == "Upload File":

    uploaded_file = st.file_uploader(
        "Upload Video/Audio File",
        type=["mp3", "wav", "mp4"]
    )

    if uploaded_file:

        if st.button("Process File"):

            with st.spinner(
                "Processing file..."
            ):

                response = upload_file(
                    uploaded_file,
                    language
                )

                transcript = response.get(
                    "transcript",
                    ""
                )

                # SAVE IN SESSION

                st.session_state[
                    "transcript"
                ] = transcript

                st.session_state[
                    "video_id"
                ] = response.get(
                    "video_id"
                )

                st.success(
                    "Transcription Completed!"
                )

                st.text_area(
                    "Transcript",
                    transcript,
                    height=300
                )

# ---------------- YOUTUBE ---------------- #

else:

    youtube_url = st.text_input(
        "Enter YouTube URL"
    )

    if st.button(
        "Process YouTube Video"
    ):

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

            # SAVE IN SESSION

            st.session_state[
                "transcript"
            ] = transcript

            st.session_state[
                "video_id"
            ] = response.get(
                "video_id"
            )

            st.success(
                "YouTube Processing Completed!"
            )

            st.text_area(
                "Transcript",
                transcript,
                height=300
            )

# ---------------- SUMMARY ---------------- #

if (
    "transcript" in st.session_state
    and
    "video_id" in st.session_state
):

    transcript = st.session_state[
        "transcript"
    ]

    video_id = st.session_state[
        "video_id"
    ]

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Generate Summary"
        ):

            with st.spinner(
                "Generating Summary..."
            ):

                response = generate_summary(
                    video_id,
                    transcript
                )

                st.subheader(
                    "Summary"
                )

                st.write( 
                    response.get("summary", "Summary generation failed")
)

    with col2:

        if st.button(
            "Generate Title"
        ):

            with st.spinner(
                "Generating Title..."
            ):

                response = generate_title(
                    transcript
                )

                st.subheader(
                    "Generated Title"
                )

                st.write( 
                    response.get("title", "Title generation failed")
                )

