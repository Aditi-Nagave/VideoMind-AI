# frontend/components/sidebar.py
import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("🎥 VideoMind AI")

        st.markdown("---")

        st.subheader("📌 Features")

        st.markdown("""
        ✅ Upload Video/Audio  
        ✅ YouTube Processing  
        ✅ AI Summarization  
        ✅ AI Chat  
        ✅ Action Item Extraction  
        ✅ Decision Extraction  
        ✅ Question Extraction  
        """)

        st.markdown("---")

        st.subheader("📂 Session Info")

        if "transcript" in st.session_state:

            transcript = st.session_state["transcript"]

            st.success("Transcript Available")

            st.write(
                f"Transcript Length: {len(transcript)} characters"
            )

        else:

            st.warning("No Transcript Loaded")

        st.markdown("---")

        if st.button("🗑 Clear Session"):

            st.session_state.clear()

            st.success("Session Cleared")

        st.markdown("---")

        st.caption(
            "Built using FastAPI + Streamlit + LangChain"
        )

