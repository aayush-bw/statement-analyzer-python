from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# loading the model - took me a while to figure out which one to use
# distilbert works well and is not too heavy
model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_sentiment(text):
    output = model(text[:512])[0]
    label = output['label']
    score = output['score']
    confidence = round(score * 100, 2)

    if confidence < 65:
        return {
            "sentiment": "Neutral",
            "confidence": confidence,
            "label": label
        }

    if label == "POSITIVE":
        sentiment = "Positive"
    else:
        sentiment = "Negative"

    return {
        "sentiment": sentiment,
        "confidence": confidence,
        "label": label
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "Please enter some text"}), 400

    if len(text) < 3:
        return jsonify({"error": "Text is too short"}), 400

    result = get_sentiment(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
