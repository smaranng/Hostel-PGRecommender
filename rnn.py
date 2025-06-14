import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn import functional as F

# Sample comments and their corresponding true labels
comments = [
    "I absolutely love this product!",  # Positive
    "The service was horrible.",       # Negative
    "It was okay, not great but not terrible.",  # Neutral
    "Best experience ever!",           # Positive
    "I would not recommend this to anyone.",  # Negative
    "This is a game-changer, well done!",  # Positive
    "It didn't meet my expectations.",  # Negative
    "Amazing quality and fast delivery!",  # Positive
    "I am very disappointed with this purchase.",  # Negative
    "Fantastic! I'll buy again."       # Positive
]

# Simulated true labels (0: Negative, 1: Neutral, 2: Positive)
true_labels = [2, 0, 1, 2, 0, 2, 0, 2, 0, 2]  # Replace with actual data if available

# Load pre-trained BERT tokenizer and model for sentiment classification
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)

# Prepare the data: Tokenize the comments
def tokenize_comments(comments):
    return tokenizer(comments, padding=True, truncation=True, max_length=512, return_tensors="pt")

# Tokenize the input comments
inputs = tokenize_comments(comments)

# Run the model in inference mode
with torch.no_grad():
    outputs = model(**inputs)

# Get the predicted labels
logits = outputs.logits
predictions = torch.argmax(F.softmax(logits, dim=-1), dim=-1)

# Map the predicted label indices to actual sentiment labels
label_mapping = {0: "Negative", 1: "Neutral", 2: "Positive"}

# Convert predictions to actual sentiment labels
mapped_predictions = [label_mapping[label.item()] for label in predictions]

# Display results and calculate accuracy
correct_predictions = 0
for true, predicted in zip(true_labels, predictions):
    if true == predicted.item():
        correct_predictions += 1

accuracy = correct_predictions / len(true_labels)

# Display results
for comment, sentiment in zip(comments, mapped_predictions):
    print(f"Comment: {comment}\nPredicted Sentiment: {sentiment}\n")

print(f"Accuracy: {accuracy * 100:.2f}%")
