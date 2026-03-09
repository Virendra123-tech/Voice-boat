User Audio
   ↓
Speech Recognition (Whisper ASR)
   ↓
Text
   ↓
Intent Classification (Transformer Model)
   ↓
Response Generation
   ↓
Text-to-Speech (gTTS)
   ↓
Audio Response
Clone the repository
git clone https://github.com/Virendra123-tech/Voice-boat
cd voicebot
Create Virtual Environment
python -m venv venv
Activate it
venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Install FFmpeg
conda install -c conda-forge ffmpeg
Run the Server
uvicorn App.main:app --reload

