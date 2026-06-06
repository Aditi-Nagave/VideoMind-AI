# frontend/pages/Signup.py
import streamlit as st

from utils.api import signup

st.title("📝 Signup")

name = st.text_input(
    "Name"
)

email = st.text_input(
    "Email"
)

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Signup"):

    result = signup(
        name,
        email,
        password
    )

    if "message" in result:

        st.success(
            result["message"]
        )

        st.info(
            "Please Login"
        )

        st.switch_page(
            "pages/Login.py"
        )

    else:

        st.error(
            result.get(
                "detail",
                "Signup Failed"
            )
        )