from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create an app instance
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotion values from the response dictionary
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]

    # Format the response for the client
    formatted_response = f"For the given statement, the "\
        f"system response is 'anger': {anger}, 'disgust': "\
        f"{disgust}, 'fear': {fear}, 'joy': {joy} and "\
        f"'sadness': {sadness}. The dominant emotion is "\
        f"{response['dominant_emotion']}." 

    return formatted_response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)