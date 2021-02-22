#  -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:13:26 2019

@author: Lenovo
"""

#just recognition of voice offline we used method recognize_sphinx()
# to use microphone we use microphone class and we take input from microphone-----install PyAudio package

import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:    
    print("speak anything u want")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio,language="en_in")
        print(f"you said {text}")
    except:
        print("sorry could not recognize your voice")
        
        
        
        
        