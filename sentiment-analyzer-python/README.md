# Sentiment Analyzer Web App

A web app that takes any text as input and tells you whether the sentiment is positive, negative, or neutral. Built using Python and Flask for the backend, and HTML/CSS/JavaScript for the frontend.

Tech used: Python, Flask, HuggingFace Transformers, HTML, CSS, JavaScript



## How to run this project

First install the required libraries:

    pip3 install flask transformers torch

Then run the app:

    python3 app.py

Open your browser and go to:

    http://127.0.0.1:5000



## Project Structure

    sentiment-analyzer/
        app.py               - Flask backend
        requirements.txt     - Libraries needed
        README.md            - This file
        templates/
            index.html       - Frontend (HTML, CSS, JavaScript)



## How it works

The user types any text into the input box on the webpage. The frontend sends that text to the Flask backend using a POST request. The backend passes the text through a pre-trained DistilBERT model from HuggingFace which predicts the sentiment and returns a confidence score. The result is then displayed on the screen.



## Libraries used

- Flask - to create the web server and API
- HuggingFace Transformers - to load and run the NLP model
- PyTorch - required by the Transformers library

## Author
Ayush Bhardwaj