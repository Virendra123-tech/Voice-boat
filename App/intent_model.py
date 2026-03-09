from transformers import pipeline

classifier = pipeline("text-classification")

def predict_intent(text):

    result = classifier(text)

    intent = result[0]["label"]
    score = result[0]["score"]

    return intent, score