from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

# Initialize Flask application
app = Flask(__name__)

# Load the pre-trained model and tokenizer
MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

# Function to predict sentiment
def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors='pt')
    outputs = model(**inputs)
    logits = outputs.logits
    probs = torch.softmax(logits, dim=-1).detach().numpy()[0]
    predicted_class = np.argmax(probs)
    labels = ['negative', 'neutral', 'positive']
    return labels[predicted_class], probs

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for sentiment prediction
@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    sentiment, probs = predict_sentiment(text)
    return jsonify({'sentiment': sentiment, 'probs': probs.tolist()})

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
