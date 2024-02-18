# pip install streamlit langchain openai wikipedia chromadb 

import os
import streamlit as st
import openai , langchain, wikipedia, chromadb
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Title
st.title("YouTube Title Suggestor 📺")
prompt = st.text_input('What\'s Your YouTube Video About ?')

# Prompt Template
title_template = PromptTemplate(input_variables=['topic'],
                                template='Suggest A Youtube Video Title About {topic}')

# Create LLM Connection
# C:/Users/aksha/AppData/Local/nomic.ai/GPT4All/
api_key = os.getenv('OpenAI_API_Key') 
LLM = OpenAI(temperature=0.9)
Title_Chain = LLMChain(llm=LLM,prompt=title_template,verbose=True,output_key='title')
  
# Show Output - Title Suggestion Only
if prompt:
    response = Title_Chain.run(topic = prompt)
    st.write(response)