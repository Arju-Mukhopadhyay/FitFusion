import pickle
import json
import numpy as np
import os
import random

# Load the model and vectorizer
with open('model/classifier.pkl', 'rb') as f:
    vectorizer, model = pickle.load(f)

# Load intents data
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "training_data", "intents.json")

with open(file_path) as f:
    data = json.load(f)

# Main response function
def get_response(text):
    text = text.lower().strip()  # ✅ Normalize user input
    X = vectorizer.transform([text])
    probs = model.predict_proba(X)[0]  # Get prediction probabilities
    tag_index = np.argmax(probs)
    confidence = probs[tag_index]
    
    tag = model.classes_[tag_index]  # ✅ Assign tag before printing
    print(f"User input: {text}")
    print(f"Predicted tag: {tag} | Confidence: {confidence}")

    if confidence < 0.1:
        return "I'm not sure I understood that. Can you rephrase?"

    for intent in data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

    return "I'm not sure how to help with that."
