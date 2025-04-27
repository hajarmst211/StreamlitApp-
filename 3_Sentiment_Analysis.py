# Pages/3_Sentiment_Analysis.py
import streamlit as st
from Utils import fetch_reviews
from transformers import pipeline

st.title("Sentiment Analysis")

app_id = st.text_input("Enter App ID to analyze reviews:")

if app_id:
    reviews = fetch_reviews(app_id)

    # Load a pre-trained sentiment analysis model from HuggingFace
    sentiment_model = pipeline("sentiment-analysis")

    # Analyze the sentiment of reviews
    sentiments = reviews['review_text'].apply(lambda x: sentiment_model(x)[0]['label'])
    reviews['sentiment'] = sentiments

    st.dataframe(reviews)

    # Visualize Sentiment Analysis
    sentiment_counts = reviews['sentiment'].value_counts()
    st.bar_chart(sentiment_counts)
