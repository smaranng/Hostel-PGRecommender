import streamlit as st
import pandas as pd
from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import matplotlib.pyplot as plt
from transformers import pipeline, BertTokenizer, BertForSequenceClassification
import torch
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os
from tensorflow.keras.models import load_model
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text_data(text):
    # 1. Lowercase conversion
    text = text.lower()
    
    # 2. Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    
    # 3. Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # 4. Remove special characters, numbers, and punctuation
    text = re.sub(r'[^a-z\s]', '', text)
    
    # 5. Tokenization
    tokens = word_tokenize(text)
    
    # 6. Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # 7. Rejoin tokens into a single string
    processed_text = ' '.join(tokens)
    return processed_text
# Function to read comments and ratings from an Excel file
def read_comments_and_ratings_from_excel(file_path, sheet_name, comments_column, ratings_column):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    comments = df[comments_column].dropna().tolist()
    ratings = df[ratings_column].dropna().tolist()
    preprocessed_comments = [preprocess_text_data(comment) for comment in comments]
    preprocessed_comments = [comment for comment in preprocessed_comments if comment]
    # Preprocess comments and drop null or empty entries
   
    return preprocessed_comments, ratings

# Function to perform sentiment analysis using RoBERTa on comments
def analyze_sentiment_roberta(comments):
    sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
    sentiments = sentiment_pipeline(comments)
    return sentiments

# Function to perform sentiment analysis using VADER on comments
def analyze_sentiment_vader(comments):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []
    for comment in comments: 
        score = analyzer.polarity_scores(comment)
        if score['compound'] >= 0.05:
            sentiments.append({'label': 'Positive'})
        elif score['compound'] <= -0.05:
            sentiments.append({'label': 'Negative'})
        else:
            sentiments.append({'label': 'Neutral'})
    return sentiments

# Function to perform sentiment analysis using TextBlob on comments
def analyze_sentiment_textblob(comments):
    sentiments = []
    for comment in comments:
        analysis = TextBlob(comment)
        if analysis.sentiment.polarity > 0:
            sentiments.append({'label': 'Positive'})
        elif analysis.sentiment.polarity < 0:
            sentiments.append({'label': 'Negative'})
        else:
            sentiments.append({'label': 'Neutral'})
    return sentiments

def analyze_sentiment_bert(comments):
    # Load pretrained BERT model and tokenizer from Hugging Face
    model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
    model = BertForSequenceClassification.from_pretrained(model_name)
    tokenizer = BertTokenizer.from_pretrained(model_name)

    # Tokenize input comments
    inputs = tokenizer(comments, return_tensors="pt", padding=True, truncation=True)

    # Perform sentiment analysis
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=-1)
    
    sentiments = []
    for prediction in predictions:
        if prediction == 4:
            sentiments.append({'label': 'Very Positive'})
        elif prediction == 3:
            sentiments.append({'label': 'Positive'})
        elif prediction == 2:
            sentiments.append({'label': 'Neutral'})
        elif prediction == 1:
            sentiments.append({'label': 'Negative'})
        else:
            sentiments.append({'label': 'Very Negative'})
    
    return sentiments

def load_pretrained_model():
    model = tf.keras.models.load_model('pg_hostel_sentiment_model.h5')  # Replace with actual path if necessary
    with open('tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
    with open('label_encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)
    return model, tokenizer, label_encoder

# Function to preprocess text (tokenize and pad)
def preprocess_text(text, tokenizer, max_len=100):
    sequences = tokenizer.texts_to_sequences(text)
    padded_sequences = pad_sequences(sequences, maxlen=max_len)
    return padded_sequences

# Function to predict sentiment using the pretrained model
def predict_sentiment(comments, model, tokenizer, label_encoder):
    # Preprocess comments
    padded_comments = preprocess_text(comments, tokenizer)
    
    # Make predictions
    predictions = model.predict(padded_comments)
    predicted_classes = predictions.argmax(axis=-1)  # Get the index of the maximum predicted value

    # Decode the predicted classes to sentiment labels
    decoded_sentiments = label_encoder.inverse_transform(predicted_classes)
    
    # Format the results like TextBlob style
    sentiments = [{'label': sentiment} for sentiment in decoded_sentiments]
    
    return sentiments

# Function to categorize sentiment scores
def categorize_sentiment(sentiment_label): # RoberTa
    if sentiment_label == "LABEL_2" or sentiment_label == "Positive":  # Very Positive
        return 5
    elif sentiment_label == "LABEL_1":  # Positive
        return 4
    elif sentiment_label == "LABEL_0" or sentiment_label == "Neutral":  # Neutral
        return 3
    elif sentiment_label == "LABEL_-1" or sentiment_label == "Negative":  # Negative
        return 2
    elif sentiment_label == "LABEL_-2":  # Very Negative
        return 1

def categorize_sentiment_rnn(sentiment_label): # RoberTa
    if sentiment_label == "very positive":  # Very Positive
        return 5
    elif sentiment_label == "positive":  # Positive
        return 4
    elif sentiment_label == "neutral":  # Neutral
        return 3
    elif sentiment_label == "negative":  # Negative
        return 2
    elif sentiment_label == "very negative":  # Very Negative
        return 1
# Function to calculate average rating from numeric ratings
def calculate_average_rating(ratings):
    numeric_ratings = []
    for rating in ratings:
        try:
            numeric_ratings.append(float(rating))
        except ValueError:
            print(f"Skipping non-numeric rating: {rating}")
    average_rating = sum(numeric_ratings) / len(numeric_ratings) if numeric_ratings else 0
    return average_rating

def display_graphs(categorized_sentiments, numeric_ratings):
    # Filter out None values from categorized_sentiments
    categorized_sentiments_filtered = [sentiment for sentiment in categorized_sentiments if sentiment is not None]
    
    # Filter out non-numeric ratings
    numeric_ratings = [float(rating) for rating in numeric_ratings if str(rating).replace('.', '', 1).isdigit()]

    # Calculate average numeric rating
    avg_numeric = sum(numeric_ratings) / len(numeric_ratings) if numeric_ratings else 0
    
    sentiment_labels = ['1-Very Negative', '2-Negative', '3-Neutral', '4-Positive', '5-Very Positive']
    sentiment_counts = pd.Series(categorized_sentiments_filtered).value_counts(sort=False)

    # Ensure sentiment_counts aligns with sentiment_labels
    sentiment_counts = [sentiment_counts.get(i, 0) for i in range(1, 6)]

    fig, ax = plt.subplots(1, 3, figsize=(24, 8))  # Adjusted from (18, 6)

    # Sentiment distribution
    ax[0].bar(sentiment_labels, sentiment_counts, color='skyblue')
    ax[0].set_title('Sentiment Distribution')
    ax[0].set_xlabel('Sentiment Categories')
    ax[0].set_ylabel('Count')
    ax[0].tick_params(axis='x', rotation=45)

    # Ratings distribution
    ax[1].hist(numeric_ratings, bins=5, color='orange', edgecolor='black')
    ax[1].set_title('Ratings Distribution')
    ax[1].set_xlabel('Ratings')
    ax[1].set_ylabel('Frequency')

    # Average ratings comparison
    avg_categorized = sum(categorized_sentiments_filtered) / len(categorized_sentiments_filtered) if categorized_sentiments_filtered else 0
    ax[2].bar(['Categorized Sentiment', 'Numeric Ratings'], [avg_categorized, avg_numeric], color=['blue', 'green'])
    ax[2].set_title('Average Ratings')
    ax[2].set_ylabel('Rating')

    plt.tight_layout()
    st.pyplot(fig)

# Location to hostels mapping
location_hostels = {
    "Jayanagar": ["CMA Boys Hostel", "ECO PG Hostels Jayanagar","Prakruthi Youth Hostel"],
    "Indiranagar": ["The Hosteller Bangalore, Indiranagar", "Zostel Bangalore (Indiranagar)","WOKE - Indiranagar, Bangalore"],
    "Rajajinagar": ["Poorna Bodha PG","Balaji Hostels for Women & Paying Guest","Sri Adichunchanagiri Free Hostel For Girls","Sri Varshini PG For Gents"],
    "Basaveshwar Nagar": ["Sai Shardhamba Ladies PG","Priya Executive PG (for Ladies)","Kambi Siddaramanna Hostel ಕಂಬಿ ಸಿದ್ದರಾಮಣ್ಣ ವಿದ್ಯಾರ್ಥಿ ನಿಲಯ"],
    "Sanjay Nagar": ["Zolo Paradise - PG in Sanjay nagar", "Sri Sai Luxurious Guest House","Zolo Mishal PG in Mathikere | Coliving PG"],
    "Banashankari 2nd Stage": ["Guru Sri gents pg","The Beehive Hostel Luxury mens PG","Padma Ladies PG"],
    "Vijayanagar":["Mathru Priya Ladies Hostel","Shri Jagatjyothi Basaveshwara Hostel,manuvana,vijayanagar",],
    "Mahalakshmi Layout":["Zolo Splendour - PG","Sri Sai PG Accommodation For Men"],
    "BTM Layout":["Zolo Hibiscus ","The Little Blue Window Hostel","Zolo Asha"],
    "JP Nagar":["S.S Boys PG - JP Nagar","Jain Student Hostel","Shirdi sai mansion pg"],
    "Banashankari 3rd Stage": ["MEERA PAYING GUEST ACCOMODATION FOR LADIES"],

}

# Mapping hostels to their corresponding Excel files
hostel_files = {
    "CMA Boys Hostel": "cma.xlsx",
    "ECO PG Hostels Jayanagar": "eco.xlsx",
    "Prakruthi Youth Hostel":"prakruti.xlsx",
    "The Hosteller Bangalore, Indiranagar": "hosteller.xlsx",
    "Zostel Bangalore (Indiranagar)":"zostel-indiranagar.xlsx",
    "WOKE - Indiranagar, Bangalore": "woke.xlsx",
    "Poorna Bodha PG": "poornabodha.xlsx",
    "Balaji Hostels for Women & Paying Guest": "balaji_women.xlsx",
    "Sri Adichunchanagiri Free Hostel For Girls": "adichunchungiri.xlsx",
    "Sai Shardhamba Ladies PG": "sai_sharadamba.xlsx",
    "Zolo Paradise - PG in Sanjay nagar":"ZOLOPARADISE.xlsx",
    "Sri Sai Luxurious Guest House":"srisailux.xlsx",
    "Guru Sri gents pg": "guru.xlsx",
    "Mathru Priya Ladies Hostel": "mathru.xlsx",
    "MEERA PAYING GUEST ACCOMODATION FOR LADIES": "Meera.xlsx",
    "Shri Jagatjyothi Basaveshwara Hostel,manuvana,vijayanagar":"jagat.xlsx",
    "Priya Executive PG (for Ladies)": "priya_executivepg.xlsx",
    "The Beehive Hostel Luxury mens PG": "beehive.xlsx",
    "Kambi Siddaramanna Hostel ಕಂಬಿ ಸಿದ್ದರಾಮಣ್ಣ ವಿದ್ಯಾರ್ಥಿ ನಿಲಯ": "kambi_siddarama.xlsx",
    "Padma Ladies PG":"padma.xlsx",
    "Sri Varshini PG For Gents":"sri_varshini.xlsx",
    "Zolo Splendour - PG": "zolo-splendor(yashwanthpur).xlsx",
    "Sri Sai PG Accommodation For Men":"sri_sai_accomodation.xlsx",
    "Zolo Hibiscus ":"  ZOLOHIBISCUS.xlsx",
    "The Little Blue Window Hostel":"littleblue.xlsx",
    "Zolo Mishal PG in Mathikere | Coliving PG":"zolomishal.xlsx",
    "S.S Boys PG - JP Nagar":"SSBoys.xlsx",
    "Jain Student Hostel":"Jain.xlsx",
    "Shirdi sai mansion pg":"SSM.xlsx",
    "Zolo Asha": "ZOLOASHA.xlsx"
}

def main():
    st.markdown(
        """
        <style>
        .main {
            background-color: #003366;
            color: white;
        }
        h1 {
            color: white;
            font-weight: bold;
        }
        h2 {
            color: white;
            font-weight: bold;
        }
        .comment {
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #1a1a1a;
            color: white;
        }
        .average-rating {
            margin-top: 20px;
            font-size: 18px;
        }
        .stMarkdown h3 {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('Hostel and PG Tracker')
    st.header('Sentiment Analysis')

    # Sidebar for model selection
    model_choice = st.sidebar.selectbox(
        "Choose Sentiment Analysis Model",
        ("RoBERTa", "VADER", "TextBlob","BERT","RNN")
    )
    # Load the pretrained RNN model, tokenizer, and label encoder
    if model_choice == "RNN":
        model, tokenizer, label_encoder = load_pretrained_model()

        
    location = st.selectbox("Select Location", list(location_hostels.keys()))
    if location:
        # Hostel selection based on location
        hostels = location_hostels.get(location, [])
        hostel = st.selectbox("Select Hostel", hostels)

        # Add a button to trigger analysis
        analyze_button = st.button("Analyze")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        if analyze_button and hostel:
            # Path to the selected hostel's Excel file
            file_path = hostel_files.get(hostel, None)
            if file_path:
                # Read comments and ratings from the Excel file
                comments, ratings = read_comments_and_ratings_from_excel(file_path, sheet_name='ExportComments.com', comments_column='Unnamed: 7', ratings_column='Unnamed: 5')
                
                # Perform sentiment analysis
                if model_choice == "RoBERTa":
                    sentiments = analyze_sentiment_roberta(comments)
                    categorized_sentiments = [categorize_sentiment(sentiment['label']) for sentiment in sentiments]
                elif model_choice == "VADER":
                    sentiments = analyze_sentiment_vader(comments)
                    categorized_sentiments = [categorize_sentiment(sentiment['label']) for sentiment in sentiments]
                elif model_choice == "TextBlob":
                    sentiments = analyze_sentiment_textblob(comments)
                    categorized_sentiments = [categorize_sentiment(sentiment['label']) for sentiment in sentiments]
                elif model_choice == "BERT":
                    sentiments = analyze_sentiment_bert(comments)
                    categorized_sentiments = [categorize_sentiment(sentiment['label']) for sentiment in sentiments]
                elif model_choice == "RNN":
                    sentiments = predict_sentiment(comments, model, tokenizer, label_encoder)  # Use RNN model
                    categorized_sentiments = [categorize_sentiment_rnn(sentiment['label']) for sentiment in sentiments]
                    
                
                st.header('Analysis: ')
                # Display comments with their sentiment analysis
                for comment, sentiment, categorized_sentiment in zip(comments, sentiments, categorized_sentiments):
                        st.markdown(
                            f"""
                            <div class="comment">
                                <p><strong>Comment:</strong> {comment}</p>
                                <p><strong>Sentiment:</strong> {sentiment['label']}</p>
                                <p><strong>Categorized Sentiment:</strong> {categorized_sentiment}</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                # Categorize sentiment scores and calculate average sentiment
                categorized_ratings = [rating for rating in categorized_sentiments if rating is not None]

                # Now calculate the average sentiment, ensuring the list is not empty
                if categorized_ratings:
                    average_sentiment = sum(categorized_ratings) / len(categorized_ratings)
                else:
                    average_sentiment = 0  # In case there are no valid ratings, set average to 0

                # Display average sentiment score
                st.markdown(f"<div class='average-rating'><strong>Average Sentiment Score:</strong> {average_sentiment:.2f}</div>", unsafe_allow_html=True)

                # Calculate and display average rating
                average_rating = calculate_average_rating(ratings)
                st.markdown(f"<div class='average-rating'><strong>Average Numeric Rating:</strong> {average_rating:.2f}</div>", unsafe_allow_html=True)
                st.subheader("Visualizations")
                display_graphs(categorized_sentiments, ratings)
if __name__ == "__main__":
    main()