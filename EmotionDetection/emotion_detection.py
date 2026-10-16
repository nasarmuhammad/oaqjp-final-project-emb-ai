"""Emotion detection using the IBM Watson NLP API."""

import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADERS = {
    "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion."""
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url=WATSON_URL,
        headers=HEADERS,
        json=payload,
        timeout=20
    )

    response.raise_for_status()

    emotion_scores = response.json()["emotionPredictions"][0]["emotion"]

    result = {
        "anger": emotion_scores["anger"],
        "disgust": emotion_scores["disgust"],
        "fear": emotion_scores["fear"],
        "joy": emotion_scores["joy"],
        "sadness": emotion_scores["sadness"]
    }

    result["dominant_emotion"] = max(
        emotion_scores,
        key=emotion_scores.get
    )

    return result
