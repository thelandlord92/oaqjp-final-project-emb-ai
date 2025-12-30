"""
Flask app for emotion detection.

Exposes:
- /emotionDetector?textToAnalyze=...
- /
"""

from __future__ import annotations

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route() -> str:
    """Analyze the provided text and return emotion scores plus the dominant one."""
    text_to_analyze = request.args.get("textToAnalyze", "", type=str).strip()

    if not text_to_analyze:
        return "Invalid text! Please try again!."

    response = emotion_detector(text_to_analyze)

    dominant = response.get("dominant_emotion")
    if dominant is None:
        return "Invalid text! Please try again!."

    formatted_response = (
        "For the given statement, the system response is "
        f"'anger': {response.get('anger')}, "
        f"'disgust': {response.get('disgust')}, "
        f"'fear': {response.get('fear')}, "
        f"'joy': {response.get('joy')} and "
        f"'sadness': {response.get('sadness')}. "
        f"The dominant emotion is {dominant}."
    )
    return formatted_response


@app.route("/")
def render_index_page() -> str:
    """Render the index page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
