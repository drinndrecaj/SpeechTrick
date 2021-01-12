import speech_recognition as speech
from selenium import webdriver

rec = speech.Recognizer()

phone = speech.Microphone()

print('starting..')

with phone as command:

audio = rec.listen(command)

print('end..')

print(rec.recognize_google(audio))

if "open Google" in rec.recognize_google(audio):
	driver = webdriver.Chrome()
if "open Firefox" in rec.recognize_google(audio):
	driver = webdriver.Firefox()
