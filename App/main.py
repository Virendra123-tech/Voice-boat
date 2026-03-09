from fastapi import FastAPI, UploadFile, File
from App.whisper_asr import transcribe_audio
from App.intent_model import predict_intent
from App.response_generator import generate_response
from App.tts_engine import text_to_speech
import os

app = FastAPI()

@app.post("/voicebot")
async def voicebot(file: UploadFile = File(...)):

    audio_path = os.path.join("test_audio", file.Recording)

    with open(audio_path, "wb") as f:
        f.write(await file.read())

    text = transcribe_audio(audio_path)

    intent, score = predict_intent(text)

    response = generate_response(intent)

    audio_file = text_to_speech(response)

    return {
        "transcribed_text": text,
        "intent": intent,
        "confidence": score,
        "response": response,
        "audio_file": audio_file
    }
