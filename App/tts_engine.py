from gtts import gTTS

def text_to_speech(text):

    tts = gTTS(text)

    file_path = "response.mp3"

    tts.save(file_path)

    return file_path