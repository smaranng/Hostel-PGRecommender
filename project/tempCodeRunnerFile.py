import streamlit as st
import pandas as pd
from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Function to read comments and ratings from an Excel file
def read_comments_and_ratings_from_excel(file_path, sheet_name, comments_column, ratings_column):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    comments = df[comments_column].dropna().tolist()
    ratings = df[ratings_column].dropna().tolist()
    return comments, ratings

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

# Function to categorize sentiment scores
def categorize_sentiment(sentiment_label):
    if sentiment_label == "LABEL_2" or sentiment_label == "Positive":  # Very Positive / Positive
        return 5
    elif sentiment_label == "LABEL_1":  # Positive
        return 4
    elif sentiment_label == "LABEL_0" or sentiment_label == "Neutral":  # Neutral
        return 3
    elif sentiment_label == "LABEL_-1" or sentiment_label == "Negative":  # Negative
        return 2
    elif sentiment_label == "LABEL_-2":  # Very Negative
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

# Location to hostels mapping
location_hostels = {
    "Jayanagar": ["CMA Boys Hostel", "ECO PG Hostels Jayanagar","Prakruthi Youth Hostel"],
    "Indiranagar": ["The Hosteller Bangalore, Indiranagar", "Zostel Bangalore (Indiranagar)","WOKE - Indiranagar, Bangalore"],
    "Rajajinagar": ["Poorna Bodha PG","Balaji Hostels for Women & Paying Guest","Sri Adichunchanagiri Free Hostel For Girls","Sri Varshini PG For Gents"],
    "Basaveshwar Nagar": ["Sai Shardhamba Ladies PG","Priya Executive PG (for Ladies)","Kambi Siddaramanna Hostel ಕಂಬಿ ಸಿದ್ದರಾಮಣ್ಣ ವಿದ್ಯಾರ್ಥಿ ನಿಲಯ"],
    "Sanjay Nagar": ["Zolo Paradise - PG in Sanjay nagar", "Sri Sai Luxurious Guest House","Zolo Mishal PG in Mathikere | Coliving PG"],
    "Banashankari 2nd Stage": ["Guru Sri gents pg","The Beehive Hostel Luxury mens PG","Yadava Hostel"],
    "Vijayanagar":["Mathru Priya Ladies Hostel","Shri Jagatjyothi Basaveshwara Hostel,manuvana,vijayanagar",],
    "Mahalakshmi Layout":["Zolo Splendour - PG","Sri Sai PG Accommodation For Men"],
    "BTM Layout":["Zolo Hibiscus ","The Little Blue Window Hostel"],
    "JP Nagar":["S.S Boys PG - JP Nagar","Jain Student Hostel","Shirdi sai mansion pg"]
    # Add other locations and hostels here
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
    "Zolo Paradise - PG in Sanjay nagar":" ",
    "Sri Sai Luxurious Guest House":" ",
    "Guru Sri gents pg": " ",
    "Mathru Priya Ladies Hostel": "mathru.xlsx",
    "Shri Jagatjyothi Basaveshwara Hostel,manuvana,vijayanagar":"jagat.xlsx",
    "Priya Executive PG (for Ladies)": "priya_executivepg.xlsx",
    "The Beehive Hostel Luxury mens PG": "",
    "Kambi Siddaramanna Hostel ಕಂಬಿ ಸಿದ್ದರಾಮಣ್ಣ ವಿದ್ಯಾರ್ಥಿ ನಿಲಯ": "kambi_siddarama.xlsx",
    "Yadava Hostel":"yadava.xlsx",
    "Sri Varshini PG For Gents":"sri_varshini.xlsx",
    "Zolo Splendour - PG": "zolo-splendor(yashwanthpur).xlsx",
    "Sri Sai PG Accommodation For Men":"sri_sai_accomodation.xlsx",
    "Zolo Hibiscus ":"",
    "The Little Blue Window Hostel":"",
    "Zolo Mishal PG in Mathikere | Coliving PG":"",
    "S.S Boys PG - JP Nagar":"",
    "Jain Student Hostel":"",
    "Shirdi sai mansion pg":""

    # Add other hostels and their files here
}

# Streamlit App
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
        ("RoBERTa", "VADER", "TextBlob")
    )

    # Location selection
    location = st.selectbox("Select Location", list(location_hostels.keys()))
    if location:
        # Hostel selection based on location
        hostels = location_hostels.get(location, [])
        hostel = st.selectbox("Select Hostel", hostels)

        if hostel:
            # Path to the selected hostel's Excel file
            file_path = hostel_files.get(hostel, None)
            if file_path:
                # Read comments and ratings from the Excel file
                comments, ratings = read_comments_and_ratings_from_excel(file_path, sheet_name='ExportComments.com', comments_column='Unnamed: 7', ratings_column='Unnamed: 5')

                # Perform sentiment analysis based on selected model
                if model_choice == "RoBERTa":
                    sentiments = analyze_sentiment_roberta(comments)
                elif model_choice == "VADER":
                    sentiments = analyze_sentiment_vader(comments)
                elif model_choice == "TextBlob":
                    sentiments = analyze_sentiment_textblob(comments)

                # Categorize sentiment scores
                categorized_sentiments = [categorize_sentiment(sentiment['label']) for sentiment in sentiments]

                # Calculate average categorized sentiment rating
                average_categorized_sentiment = sum(categorized_sentiments) / len(categorized_sentiments) if categorized_sentiments else 0

                # Calculate average numeric rating
                average_numeric_rating = calculate_average_rating(ratings)

                # Display sentiment analysis results
                st.markdown('<h3>Sentiment Analysis Results</h3>', unsafe_allow_html=True)
                if comments:
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
                else:
                    st.text('No comments found.')

                # Display average ratings
                st.markdown('<h3>Average Ratings</h3>', unsafe_allow_html=True)
                st.text(f'Average Categorized Sentiment Rating: {average_categorized_sentiment:.2f}')
                st.text(f'Average Numeric Rating: {average_numeric_rating:.2f}')
            else:
                st.text('No Excel file found for the selected hostel.')

if __name__ == '__main__':
    main()
