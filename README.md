# Sentiment Analyzer Web App

A web-based application that analyzes user input text and classifies it as **positive, negative, or neutral sentiment** using a  NLP model.

This project uses a **DistilBERT model from HuggingFace Transformers** to provide accurate sentiment predictions along with confidence scores.



## Features

* Real-time sentiment analysis via web interface
* Uses  Transformer model (DistilBERT)
* Displays sentiment with confidence score
* Simple and responsive UI

---

## Tech Stack

* **Backend:** Python, Flask
* **NLP Model:** HuggingFace Transformers (DistilBERT)
* **Frontend:** HTML, CSS, JavaScript
* **Frameworks/Libraries:** PyTorch

---

## Example

Input:

```
I really enjoyed this experience!
```

Output:

```
Positive (Confidence: 0.97)
```

---

## Project Structure

```
sentiment-analyzer/
│── app.py
│── requirements.txt
│── README.md
│── templates/
│   └── index.html
```

---

## How to Run

1. Clone the repository
2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Run the application:

   ```
   python app.py
   ```
4. Open in browser:

   ```
   http://127.0.0.1:5000
   ```

---

## How It Works

* User enters text in the web interface
* Frontend sends input to Flask backend via POST request
* Backend processes text using a  DistilBERT model
* Model returns sentiment label + confidence score
* Result is displayed on the webpage

---

## Future Improvements

* Add support for batch text analysis
* Deploy as a live web application
* Improve UI/UX design

---

## Author

Aayush Bhardwaj

