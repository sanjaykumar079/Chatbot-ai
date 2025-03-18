# emotion_recognizer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
from transformers import pipeline

# Load DistilBERT for emotion detection
emotion_recognizer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def detect_emotion(text):
    """
    Detect the dominant emotion in the input text using DistilBERT.
    Returns: (emotion_label, confidence_score)
    """
    if not text or not isinstance(text, str):
        print("Invalid input text, returning default")
        return "neutral", 0.5

    predictions = emotion_recognizer(text)
    print("Raw predictions:", predictions)

    if isinstance(predictions, list) and len(predictions) > 0 and isinstance(predictions[0], dict):
        top_emotion = max(predictions, key=lambda x: x['score'])
        return top_emotion['label'], top_emotion['score']
    
    print("Warning: Unexpected output format, returning default")
    return "neutral", 0.5