import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Load the trained model and vectorizer
model_filename = 'updatedTrainedModel.sav'  # Path to the saved model file
vectorizer_filename = 'trained_count_vectorizer.pkl'  # Path to the saved vectorizer file

# Load the trained model
with open(model_filename, 'rb') as f:
    loaded_model = pickle.load(f)

# Load the fitted vectorizer
with open(vectorizer_filename, 'rb') as f:
    count_vectorizer = pickle.load(f)

# Define a function for processing text and making predictions
def process_text(text):
    # Transform the input text using the CountVectorizer
    transformed_text = count_vectorizer.transform([text])
    return transformed_text

def make_prediction(text):
    # Process the text using the loaded model
    processed_text = process_text(text)
    prediction = loaded_model.predict(processed_text)
    
    # Map prediction to sentiment label
    if prediction == 0:
        sentiment = "Negative"
    elif prediction == 1:
        sentiment = "Neutral"
    elif prediction == 2:
        sentiment = "Positive"
    return sentiment

# Streamlit application
st.title('Sentiment Analysis System')

# Create a text area for user input
user_input = st.text_area('Enter a tweet:', height=150)

# Add a button for predicting the sentiment
if st.button('Detect Sentiment'):
    if user_input.strip():  # Check if the input is not empty
        sentiment = make_prediction(user_input)
        st.write('Sentiment:', sentiment)
    else:
        st.warning('Please enter a tweet.')

# Add a footer
st.text('Developed by: Developer')