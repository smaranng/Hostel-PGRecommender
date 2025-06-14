import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle

# Step 1: Load the saved model
model = tf.keras.models.load_model('pg_hostel_sentiment_model.h5')

# Step 2: Load the tokenizer and label encoder (which were saved during training)
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Step 3: Define a function to predict sentiment
def predict_sentiment(review):
    print(f"Predicting sentiment for: {review}")

    max_len = 100  # Default padding length
    if len(review.split()) == 1:  # If the comment is a single word, use smaller padding
        max_len = 10
    tokenized_review = tokenizer.texts_to_sequences([review])
    padded_review = pad_sequences(tokenized_review, maxlen=max_len)
    prediction = model.predict(padded_review)
    sentiment_index = np.argmax(prediction)  # Get the index of the highest probability
    sentiment = label_encoder.inverse_transform([sentiment_index])[0]
    print(f"Predicted sentiment: {sentiment}")
    return sentiment

# Example test reviews
test_comments = [
    "The hostel is amazing! Very comfortable and clean.",
    "I had a terrible experience, everything was so bad.",
    "It was an average stay, nothing special but okay.",
    "I love the food here, it's always fresh and tasty.",
    "The room was too small and cramped, not ideal.",
    "good","bad","ok ok","horrible","besttt"

]

# Test the model with new reviews
for comment in test_comments:
    predicted_sentiment = predict_sentiment(comment)
