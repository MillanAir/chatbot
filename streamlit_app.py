# Import convention
import streamlit as st

st.file_uploader('File uploader')
with st.chat_message("user"):
    st.write("Hello 👋")

# Display a chat input widget.
st.chat_input("Write your query here...")