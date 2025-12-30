import requests
import json

def emotion_detector(text_to_analyze):
    """
    Defines a function for emotion detection
    of input text
    """

    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Custom header specifying the model ID for the emotion detection service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # The text to be analysed
    text_to_analyse = text_to_analyze

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json = myobj, headers=headers)

    # Parsing the JSON response from the API
    response_json = json.loads(response.text)

    # Get the emotion dictionary
    emotion_dict = response_json["emotionPredictions"][0]["emotion"]

    # Sort the emotions based on the scores to find the highest value
    emotion_list = []
    # Switch the position of the keys and values to (value, key)
    for key, value in emotion_dict.items():
        tup = (value, key)
        emotion_list.append(tup)
    sorted_emotion_list = sorted(emotion_list, reverse=True)

    # Created a formatted dictionary of the emotions
    formatted_emotion_dict = {
        "anger": emotion_dict["anger"],
        "disgust": emotion_dict["disgust"],
        "fear": emotion_dict["fear"],
        "joy": emotion_dict["joy"],
        "sadness": emotion_dict["sadness"],
        "dominant_emotion": sorted_emotion_list[0][1]
    }

    return formatted_emotion_dict
