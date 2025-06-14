import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense, Dropout, LSTM, Bidirectional,GRU
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Step 1: Load the Dataset from Excel
# Replace 'your_dataset.xlsx' with your Excel file name.
# Ensure the Excel file has columns 'Review' and 'Sentiment'
df = pd.read_excel('updated_hostel_comments.xlsx')  # Change the path to your actual file
# Print the columns to check if 'Review' and 'Sentiment' exist
print(df.columns)

# Check if the file has the correct columns
print(df.head())

# Step 2: Preprocess the Data
# 2.1 Encode Sentiments (very negative, negative, neutral, positive, very positive)
label_encoder = LabelEncoder()
df['Sentiment'] = label_encoder.fit_transform(df['Sentiment'])  # Convert sentiments to integers

# 2.2 Tokenize and Pad Reviews
vocab_size = 10000  # Vocabulary size
max_len = 100
embedding_dim = 300  # Maximum length of sequences
tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(df['Comment'].values)

X = tokenizer.texts_to_sequences(df['Comment'].values)
X = pad_sequences(X, maxlen=max_len)
y = df['Sentiment'].values

# Step 3: Split the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Build the RNN Model
model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=128, input_length=max_len),
    Bidirectional(GRU(128, return_sequences=False)),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(5, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Compile the model
optimizer = Adam(learning_rate=0.011)  # Use a lower learning rate
model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.summary()

# Step 5: Train the Model
history = model.fit(X_train, y_train, epochs=20, batch_size=100, validation_split=0.2)

# Step 6: Evaluate the Model
model.save('pg_hostel_sentiment_model.h5')

# Step 5: Save Tokenizer and Label Encoder for Later Use
with open('tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)

with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

# Step 6: Evaluate the Model
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

# Optional: Visualize Training Progress
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

print("end..")
