import streamlit as st

from utils.api import signup

st.title("📝 Signup")

name = st.text_input("Name")

email = st.text_input("Email")

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

    st.success(
        result["message"]
    )