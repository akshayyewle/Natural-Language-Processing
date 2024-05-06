# pip install streamlit langchain openai wikipedia chromadb 

import os
import streamlit as st
# import openai , langchain, wikipedia, chromadb
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utils import WikipediaAPIWrapper

# Title
st.title("YouTube Title & Script Assistant 📺")
prompt = st.text_input('What\'s Your YouTube Video About ?')
# Prompt Template
title_template = PromptTemplate(input_variables=['topic'],
                                template='Suggest A Youtube Video Title About {topic}')
script_template = PromptTemplate(input_variables=['title'],
                                template='Suggest A Youtube Video Script About {title}')

# Memory
Memory01 = ConversationBufferMemory(input_key='topic',memory_key='chat_history')

# Create LLM Connection
# C:/Users/aksha/AppData/Local/nomic.ai/GPT4All/
api_key = os.getenv('OpenAI_API_Key') 
LLM = OpenAI(temperature=0.9)
Title_Chain = LLMChain(llm=LLM,prompt=title_template,verbose=True,
                       output_key='title',memory=Memory01)
Script_Chain = LLMChain(llm=LLM,prompt=script_template,verbose=True,output_key='script',
                        memory=Memory01)
Sequential_Chain01 = SequentialChain(chains=[Title_Chain,Script_Chain],
                 input_variables=['topic'],
                 output_variables=['title','script'],
                 verbose=True)
  
# Show Output - Title & Script Suggester
if prompt:
    response = Sequential_Chain01({'topic':prompt})
    st.write(response['title'])
    st.write(response['script'])

    with st.expander("Show Chat History"):
        st.info(Memory01.buffer)