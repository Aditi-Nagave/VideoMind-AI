import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("🎥 VideoMind AI")

        st.markdown("---")

        # =========================
        # USER INFO
        # =========================

        if "user" in st.session_state:

            st.success(
                f"Logged in as: "
                f"{st.session_state['user']['name']}"
            )

            st.write(
                st.session_state["user"]["email"]
            )

            if st.button("🚪 Logout"):

                st.session_state.clear()

                st.rerun()

            st.markdown("---")

        # =========================
        # FEATURES
        # =========================

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

        # =========================
        # SESSION INFO
        # =========================

        st.subheader("📂 Session Info")

        if "transcript" in st.session_state:

            transcript = st.session_state["transcript"]

            st.success("Transcript Available")

            st.write(
                f"Transcript Length: "
                f"{len(transcript)} characters"
            )

        else:

            st.warning(
                "No Transcript Loaded"
            )

        # Video ID

        if "video_id" in st.session_state:

            st.info(
                f"Video ID: "
                f"{st.session_state['video_id']}"
            )

        st.markdown("---")

        # =========================
        # CLEAR SESSION
        # =========================

        if st.button("🗑 Clear Session"):

            token = st.session_state.get(
                "token"
            )

            user = st.session_state.get(
                "user"
            )

            st.session_state.clear()

            if token:
                st.session_state["token"] = token

            if user:
                st.session_state["user"] = user

            st.success(
                "Video Session Cleared"
            )

            st.rerun()

        st.markdown("---")

        st.caption(
            "Built using FastAPI + Streamlit + LangChain + PostgreSQL"
        )