# Import convention
import streamlit as st

st.title('SQL Chatbot')
st.file_uploader('Upload your sql files', type=['sql', 'sqlite'])
with st.chat_message("user"):
    st.write("Hello Please enter your queries below and wait for a response 👋")

# Display a chat input widget.
st.chat_input("Write your query here...")