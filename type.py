from gpthandler import *
#from tts import *
import pyttsx3
import os

#for text input

while True:
    a = input("type prompt to enter into main.py: ")
    s = speechreceived(a)
    v = pyttsx3.init()
    v.say(s)
    v.runAndWait()
    #get_tts(s)
