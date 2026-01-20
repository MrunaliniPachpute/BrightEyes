import azure.cognitiveservices.speech as speechsdk
import tempfile
import os 
from dotenv import load_dotenv
load_dotenv()

AZURE_SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
AZURE_SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION")

def speak_text_azure(text):
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_SPEECH_REGION)
    speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"
    
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        audio_config = speechsdk.audio.AudioOutputConfig(filename=f.name)
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        synthesizer.speak_text_async(text).get()
        return f.name  # path to audio file
