import streamlit as st

from utils.api import (
    login,
    get_user
)

st.title("🔐 Login")

email = st.text_input(
    "Email"
)

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    try:

        result = login(
            email,
            password
        )

        token = result["access_token"]

        user = get_user(
            token
        )

        # Save session

        st.session_state["token"] = token

        st.session_state["user"] = user

        st.success(
            "Login Successful"
        )

        st.rerun()

    except Exception:

        st.error(
            "Invalid Email or Password"
        )