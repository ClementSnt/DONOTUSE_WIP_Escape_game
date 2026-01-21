import streamlit as st

st.title("Accès")

user_input = st.text_input("Entre le mot clé")

if user_input:
    if user_input == "test":
        st.success("Oui")
    else:
        st.error("Non")
