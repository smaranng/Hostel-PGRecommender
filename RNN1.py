import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, LSTM, GRU, Bidirectional, Dense
# Load IMDB dataset
vocab_size = 10000  # Top 10,000 words
max_length = 200    # Maximum length of sequences
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocab_size)

# Pad sequences to the same length
X_train = pad_sequences(X_train, maxlen=max_length, padding='post')
X_test = pad_sequences(X_test, maxlen=max_length, padding='post')
def build_vanilla_rnn():
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=128, input_length=max_length),
        SimpleRNN(64),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
def build_lstm():
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=128, input_length=max_length),
        LSTM(64),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
def build_gru():
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=128, input_length=max_length),
        GRU(64),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
def build_bidirectional_lstm():
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=128, input_length=max_length),
        Bidirectional(LSTM(64)),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
# Example with Vanilla RNN
model = build_gru()

# Train the model
history = model.fit(X_train, y_train, validation_split=0.2, epochs=5, batch_size=32)

# Evaluate on test set
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy}')
# Plot training and validation accuracy
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

from tensorflow.keras.datasets import imdb

# Load the word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# Preprocess the comments
def preprocess_comment(comment, word_index, max_length=200):
    # Tokenize the comment
    words = comment.lower().split()
    tokenized = [word_index.get(word, 2) for word in words]  # '2' is for unknown words
    # Pad the sequence
    padded_sequence = pad_sequences([tokenized], maxlen=max_length, padding='post')
    return padded_sequence

# Two sample comments
sample_comments = [
    "The movie was fantastic and very engaging",
    "I didn't like the movie, it was boring"
]

# Preprocess and predict
for comment in sample_comments:
    sequence = preprocess_comment(comment, word_index, max_length)
    prediction = model.predict(sequence)
    sentiment = "Positive" if prediction[0] > 0.5 else "Negative"
    print(f"Comment: '{comment}'\nPredicted Sentiment: {sentiment}\nConfidence: {prediction[0][0]:.2f}\n")

