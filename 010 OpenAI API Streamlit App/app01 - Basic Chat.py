# pip install streamlit langchain openai wikipedia chromadb 

import os
import streamlit as st
import openai , langchain, wikipedia, chromadb
from langchain.llms import OpenAI

# Title
st.title("OpenAI API Chat Bot 🤖")
prompt = st.text_input('Input Text.....')

# Create LLM Connection
api_key = os.getenv('OpenAI_API_Key') 
LLM = OpenAI(temperature=0.9)

# Show Output - Basic Chat 
if prompt:
    response = LLM(prompt)
    st.write(response)