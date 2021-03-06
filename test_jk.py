#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#najpierw wy��cz
GPIO.setup(17,GPIO.OUT, initial= GPIO.LOW)
r = sr.Recognizer()
with sr.WavFile("turn_on.wav") as source:
    audio = r.record(source)

#with sr.Microphone() as source:
#    print ("Say Something")
#    audio = r.listen(source)
  

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    spokenAudio = r.recognize_google(audio)
    if spokenAudio == "turn on" :
    	print(spokenAudio)
	GPIO.setup(17,GPIO.OUT, initial= GPIO.HIGH)
    
    #print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except LookupError:
    print("Google Speech Recognition could not understand audio")



#turn off

# obtain audio from the microphone
r = sr.Recognizer()
with sr.WavFile("turn_off.wav") as source:
    audio = r.record(source)

#with sr.Microphone() as source:
#    print ("Say Something")
#    audio = r.listen(source)
  

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    spokenAudio = r.recognize_google(audio)
    if spokenAudio == "turn off" :
    	print(spokenAudio)
	GPIO.setup(17,GPIO.OUT, initial= GPIO.LOW)
    
    #print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except LookupError:
    print("Google Speech Recognition could not understand audio")
