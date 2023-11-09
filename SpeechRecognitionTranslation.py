from pydub import AudioSegment
import datetime
import sys
import google.auth
import speech_recognition as sr
from google.cloud import speech
from googletrans import Translator, constants
from deep_translator import GoogleTranslator
## make sure to install ffmpeg 

r = sr.Recognizer()
audfile = sr.AudioFile("audiofile.wav")

with audfile as source:
    audio = r.record(source)

result = r.recognize_google(audio, language= 'es-FR')
print(result)

translator = GoogleTranslator(source='auto', target='en')
translator.translate(result)