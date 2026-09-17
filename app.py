"""Gemini LLM Application - Streamlit Q&A powered by Google's Gemini model."""
import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(page_title="Gemini LLM App", page_icon=":sparkles:")
st.title("Gemini LLM Application")
st.write("Ask a question \u2014 answered by Google's Gemini model.")

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("GOOGLE_API_KEY is not set. Copy .env.example to .env and add your key.")
    st.stop()

client = genai.Client(api_key=api_key)

question = st.text_input("Your question:")
if st.button("Get Response") and question.strip():
    with st.spinner("Thinking..."):
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=question,
        )
    st.subheader("Response")
    st.write(response.text)
