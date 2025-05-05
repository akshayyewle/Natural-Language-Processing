import streamlit as st
import nltk
from nltk import sentiment
nltk.download('vader_lexicon')  

# Title   
st.title("Sentiment Analyser")

# Text Input 
input_text = st.text_input("Enter the text to be analysed", max_chars= 1000)

# Sentiment Analysis Button 
if st.button("Analyse"):

    # Initialize NLTK Sentiment Analyzer
    from nltk.sentiment import SentimentIntensityAnalyzer 
    SIA = SentimentIntensityAnalyzer()

    # Placeholder for the result
    st.write("Sentiment Analysis Result:")
    
    # Simulated result (replace with actual analysis)
    result = SIA.polarity_scores(input_text)

    # Composite Score
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Negative", result['neg'])
    col2.metric("Neutral", result['neu'])
    col3.metric("Positive", result['pos'])
    col4.metric("Compound", result['compound'])

    # Display the result horizontal bar chart
    st.bar_chart({
        'Negative': result['neg'],
        'Neutral': result['neu'],
        'Positive': result['pos']
    },horizontal=True, width = 100, height = 300)
    
    # Display the result
    st.write(result)