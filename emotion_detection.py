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

    return response.text
