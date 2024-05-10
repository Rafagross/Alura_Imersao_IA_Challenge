import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('trained_model.h5')

# Function to preprocess text
def preprocess_text(text):
    # Your text preprocessing code here
    return processed_text

# Function to make prediction
def predict_sentiment(text):
    processed_text = preprocess_text(text)
    sequence = tokenizer.texts_to_sequences([processed_text])
    padded_sequence = pad_sequences(sequence, maxlen=100, padding='post')
    prediction = model.predict(padded_sequence)
    return prediction

# Streamlit web interface
st.title('Sentiment Analysis with AI')

user_input = st.text_input('Enter the text to analyze:')
if st.button('Analyze Sentiment'):
    prediction = predict_sentiment(user_input)
    if prediction > 0.5:
        st.write('Sentiment: Positive')
    else:
        st.write('Sentiment: Negative')

