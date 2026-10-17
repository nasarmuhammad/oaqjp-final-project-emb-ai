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

EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    """Return empty scores for invalid text."""
    return {
        **dict.fromkeys(EMOTIONS),
        "dominant_emotion": None
    }


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion."""
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()

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

    if response.status_code == 400:
        return _empty_result()

    response.raise_for_status()

    emotion_scores = response.json()["emotionPredictions"][0]["emotion"]

    result = {
        emotion: emotion_scores[emotion]
        for emotion in EMOTIONS
    }

    result["dominant_emotion"] = max(
        EMOTIONS,
        key=result.get
    )

    return result
