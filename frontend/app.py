# frontend/app.py
import streamlit as st

st.set_page_config(
    page_title="VideoMind AI",
    page_icon="🎥",
    layout="wide"
)

# -------------------------
# AUTH CHECK
# -------------------------

if "token" not in st.session_state:

    st.title("🎥 VideoMind AI")

    st.markdown("""
    ## Welcome to VideoMind AI

    Please Login or Signup first.
    """)

    col1, col2 = st.columns(2)

    with col1:

        if st.button("🔐 Login"):

            st.switch_page(
                "pages/Login.py"
            )

    with col2:

        if st.button("📝 Signup"):

            st.switch_page(
                "pages/Signup.py"
            )

    st.stop()

# -------------------------
# LOGGED IN
# -------------------------

st.title("🎥 VideoMind AI")

st.success(
    f"Welcome {st.session_state['user']['name']}"
)

st.markdown("""
### Features

- Upload Video
- YouTube Processing
- AI Summarization
- AI Chat
- Action Item Extraction
- Decision Extraction
- Question Extraction
""")

if st.button("🚀 Go To Dashboard"):

    st.switch_page(
        "pages/Home.py"
    )