import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Function to read comments and ratings from an Excel file
def read_comments_and_ratings_from_excel(file_path, sheet_name, comments_column, ratings_column):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Extract comments and drop NaN values
    comments = df[comments_column].dropna().tolist()
    
    # Extract ratings and filter out non-numeric values
    ratings = df[ratings_column].dropna()
    
    # Convert ratings to numeric values, ignoring any non-numeric values
    ratings = [float(rating) for rating in ratings if str(rating).replace('.', '', 1).isdigit()]
    
    return comments, ratings

# Function to analyze sentiment using VADER
def analyze_sentiment_vader(comment):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(comment)
    compound_score = sentiment_scores['compound']
    
    if compound_score >= 0.5:
        return 5  # Very Positive
    elif compound_score >= 0.2:
        return 4  # Positive
    elif compound_score > -0.2:
        return 3  # Neutral
    elif compound_score > -0.6:
        return 2  # Negative
    else:
        return 1  # Very Negative

# Function to analyze sentiment using TextBlob
def analyze_sentiment_textblob(comment):
    analysis = TextBlob(comment)
    polarity = analysis.sentiment.polarity
    
    if polarity >= 0.5:
        return 5  # Very Positive
    elif polarity >= 0.2:
        return 4  # Positive
    elif polarity > -0.2:
        return 3  # Neutral
    elif polarity > -0.6:
        return 2  # Negative
    else:
        return 1  # Very Negative

# Path to your Excel file
file_path = 'cma.xlsx'
sheet_name = 'ExportComments.com'  # Change if your sheet name is different
comments_column = 'Unnamed: 7'  # Change if your column name is different
ratings_column = 'Unnamed: 5'  # Change if your column name is different

# Read comments and ratings from the Excel file
comments, ratings = read_comments_and_ratings_from_excel(file_path, sheet_name, comments_column, ratings_column)

# Analyze sentiment using VADER
vader_ratings = []
print("VADER Sentiment Analysis:")
for comment in comments:
    sentiment = analyze_sentiment_vader(comment)
    vader_ratings.append(sentiment)
    print(f"Comment: {comment}")
    print(f"Predicted Sentiment: {sentiment}")
    print()

# Calculate and print the average VADER rating
average_vader_rating = sum(vader_ratings) / len(vader_ratings) if vader_ratings else 0
print(f"Average VADER Rating: {average_vader_rating:.2f}")
print("*******************************************")

# Analyze sentiment using TextBlob
textblob_ratings = []
print("TextBlob Sentiment Analysis:")
for comment in comments:
    sentiment = analyze_sentiment_textblob(comment)
    textblob_ratings.append(sentiment)
    print(f"Comment: {comment}")
    print(f"Predicted Sentiment: {sentiment}")
    print()

# Calculate and print the average TextBlob rating
average_textblob_rating = sum(textblob_ratings) / len(textblob_ratings) if textblob_ratings else 0
print(f"Average TextBlob Rating: {average_textblob_rating:.2f}")
print("*******************************************")

# Calculate and print the average rating from the ratings column
average_numeric_rating = sum(ratings) / len(ratings) if ratings else 0.0  # Ensure the average is a float
print(f"Average Numeric Rating: {average_numeric_rating:.2f}")
