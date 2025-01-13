import streamlit as st
import re 
import torch
from transformers import BertTokenizer, BertModel

# Title 
st.header("Word To Numeric Vector ✍️")

# Select Voacbulary
vocabulary = st.selectbox("Select Vocabulary", ["Google BERT"])

# Load model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Input Word
input_word = st.text_input("Enter a word")
input_word_lower = input_word.lower()
input_word_cleaned = re.sub(r'[^\w\s]', '', input_word_lower)

# Button to convert word to numeric vector
if st.button("Convert"):
    # Convert word to numeric vector using the selected vocabulary
    if vocabulary == "GloVe":
        
        # Code to convert word to numeric vector using GloVe
        # pass
        st.write(input_word_cleaned)

    else:
        st.error("Invalid vocabulary selected.")

# Camera Video 
camera_video = st.camera_input(label="Camera Input")

if camera_video:
    st.image(camera_video)
