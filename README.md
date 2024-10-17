Sentiment Analysis Web App using RoBERTa
This repository contains a Flask web application that performs sentiment analysis on text input using a pre-trained RoBERTa model from Hugging Face. The app predicts whether the sentiment of the input text is positive, neutral, or negative.

Features
Web-based interface for sentiment analysis.
Uses the pre-trained cardiffnlp/twitter-roberta-base-sentiment model.
Predicts sentiment for user-submitted text.
Returns the predicted sentiment along with the probabilities for each class.

How It Works
User input: The user submits text through the web interface.
Model prediction: The text is tokenized and passed to the RoBERTa model for sentiment classification.
Response: The app returns the sentiment label (positive, neutral, negative) and the associated probabilities.

Installation and Setup
Prerequisites

Python 3.x
pip for package installation

Install the required packages
bash

pip install -r requirements.txt
The requirements.txt should contain:

txt
Copy code
Flask
torch
transformers
numpy

Running the App
Clone this repository:

bash
Copy code
git clone https://github.com/anish840/Sentimental-Analysis/tree/main
cd sentiment-analysis-flask
Run the Flask application:

bash
Copy code
python app.py
Open your browser and navigate to http://127.0.0.1:5000/ to access the app. # you will get your own local domain.

Usage
Go to the home page.
Enter a piece of text in the input field.
Click the "Analyze" button to get the sentiment prediction and probabilities.
Project Structure
php
Copy code
.
├── app.py               # Main Flask app
├── templates
│   └── index.html       # Frontend HTML file
├── static
│   └── (optional)       # Static files like CSS or JS
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
Model Details
This application uses the cardiffnlp/twitter-roberta-base-sentiment model from Hugging Face. It is a variant of the RoBERTa model fine-tuned on Twitter data to classify sentiments as positive, neutral, or negative.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or bug fixes.
