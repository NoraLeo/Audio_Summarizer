#!/usr/bin/env python3

#we wil be using SpeechRecognition library
#performing speech recognition, with support for several engines and APIs, online and offline.
#to install the library, use pip install SpeechRecognition (in Windows) or python3 -m pip install SpeechRecognition
#https://pypi.org/project/SpeechRecognition/
import speech_recognition as sr
#to receive audio input using a mic/sound recorder
import pyaudio

#there are different recognizer APIs to convert the audio signals in the audio data to text.
#but first, we need to create an instance of the main Recognizer class.

def record_audio(audio_path):
    recognizer = sr.Recognizer()
    recognizer.energy_threshold= 300
    if audio_path != "" and audio_path != None:
        with sr.AudioFile(audio_path) as source:
            #convert audio file to audio data
            #accomodate for noise
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio_file = recognizer.record(source)
        text = recognizer.recognize_google_cloud(audio_data=audio_file, credentials_json="")
        return text
    else:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Speak Anything :")
            audio_file = recognizer.listen(source)
        try:
            text = recognizer.recognize_google_cloud(audio_data=audio_file, credentials_json="")
            return text
        except:
            print("Sorry could not understand what you said!")


