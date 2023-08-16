from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI
from langchain_experimental.sql import SQLDatabaseChain
import streamlit as st

st.title("SQL Chatbot")
# Set up OpenAI API
api_key = st.text_input("Enter your OpenAI API token")

# File uploader
uploaded_file = st.file_uploader("Upload SQL or SQLite file", type=["sql", "sqlite"])

# Chat window
query = st.text_input("Enter your query")

# Submit query button
if st.button("Submit Query"):
    if uploaded_file is not None:
        if api_key is not None:
            llm = OpenAI(temperature=0, verbose=True, openai_api_key=api_key)
            # Convert uploaded file to BytesIO object
            db = SQLDatabase.from_uri("sqlite:///Chinook_SQLite")
            db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
            st.write(db_chain.run(query))  # Display the result
        else:
            st.write("Please add your OpenAI API key to continue.")
    else:
        st.write("Please upload a file first.")