import re
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import BertTokenizer, BertForSequenceClassification
import torch
from torch.nn.functional import softmax

# Define comments with ground truth labels
comments = [
    ("positive", "I love this product! It works perfectly."),  # positive
    ("negative", "This is the worst purchase I have ever made."),  # negative
    ("neutral", "The movie was okay, not great but not bad either."),  # neutral
    ("positive", "Absolutely amazing service, highly recommend!"),  # positive
    ("negative", "I hate the new update, it's so buggy."),  # negative
    ("neutral", "Not too bad, just needs a few improvements."),  # neutral
    ("negative", "Very disappointing experience, would not buy again."),  # negative
    ("positive", "This is the best book I've ever read!"),  # positive
    ("negative", "The food was bland and unappetizing."),  # negative
    ("neutral", "It's just fine, nothing special."),  # neutral
    ("positive", "Fantastic customer support, resolved my issue quickly."),  # positive
    ("negative", "I feel like I wasted my money."),  # negative
    ("neutral", "Could be better, but it's acceptable."),  # neutral
    ("positive", "A wonderful journey, loved every part of it."),  # positive
    ("negative", "Extremely frustrating, I want my money back."),  # negative
]

# Extract labels and text
ground_truth = [label for label, _ in comments]
comment_texts = [text for _, text in comments]

# Function to preprocess comments for uniformity
def preprocess_text(comments, lowercase=True, remove_punct=False):
    preprocessed_comments = []
    for comment in comments:
        if remove_punct:
            comment = re.sub(f"[{string.punctuation}]", "", comment)  # Remove punctuation
        if lowercase:
            comment = comment.lower()  # Convert to lowercase
        preprocessed_comments.append(comment.strip())
    return preprocessed_comments

# Preprocess comments for VADER (no punct removal, lowercase optional)
vader_comments = preprocess_text(comment_texts, lowercase=False, remove_punct=False)

# Preprocess comments for Transformers (punctuation removed, lowercase applied)
transformer_comments = preprocess_text(comment_texts, lowercase=True, remove_punct=True)

# --- VADER Sentiment Analysis ---
analyzer = SentimentIntensityAnalyzer()

def vader_sentiment_analysis(comments):
    results = []
    for comment in comments:
        scores = analyzer.polarity_scores(comment)
        sentiment = (
            "positive" if scores["compound"] > 0.05 else
            "negative" if scores["compound"] < -0.05 else
            "neutral"
        )
        results.append(sentiment)
    return results

vader_results = vader_sentiment_analysis(vader_comments)

# --- Transformers Sentiment Analysis ---
# Load BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)

def transformer_sentiment_analysis(comments):
    inputs = tokenizer(comments, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predictions = torch.argmax(softmax(logits, dim=1), dim=1).tolist()
    sentiments = ["negative", "neutral", "positive"]  # Label mapping
    return [sentiments[p] for p in predictions]

transformer_results = transformer_sentiment_analysis(transformer_comments)

# --- Calculate and Display Results ---
def calculate_accuracy(predictions, ground_truth):
    correct = sum([1 for pred, true in zip(predictions, ground_truth) if pred == true])
    accuracy = correct / len(ground_truth)
    return accuracy

# Calculate accuracy for VADER and Transformers
vader_accuracy = calculate_accuracy(vader_results, ground_truth)
transformer_accuracy = calculate_accuracy(transformer_results, ground_truth)

# Display results
print("Original Comments and Sentiments:\n")
for i, comment in enumerate(comment_texts):
    print(f"Comment: {comment}")
    print(f"Ground Truth: {ground_truth[i]}")
    print(f"VADER Sentiment: {vader_results[i]}")
    print(f"Transformer Sentiment: {transformer_results[i]}")
    print("-" * 50)

print(f"VADER Accuracy: {vader_accuracy * 100:.2f}%")
print(f"Transformer Accuracy: {transformer_accuracy * 100:.2f}%")
