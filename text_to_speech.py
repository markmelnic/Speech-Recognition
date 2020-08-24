
import os 
from gtts import gTTS 

with open("recognize.txt", 'r') as recFile:
    content = recFile.read()

language = 'en'
tts = gTTS(text=content, lang=language, slow=False) 
tts.save("recognize.wav") 
