import json
import numpy as np
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

nltk.download('punkt')

# Define path to training data
intent_file = r'app/chatbot/training_data/intents.json'



with open(intent_file) as f:
    data = json.load(f)

patterns = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern.lower().strip())  # ✅ normalize input
        labels.append(intent['tag'])


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)

model = MultinomialNB()
model.fit(X, labels)

# Define directory to save the model
model_dir = 'model'
os.makedirs(model_dir, exist_ok=True)

with open(os.path.join(model_dir, 'classifier.pkl'), 'wb') as f:
    pickle.dump((vectorizer, model), f)

print("Model trained and saved.")
