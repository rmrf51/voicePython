import speech_recognition as sr 
import os
import sys
import webbrowser
import pyttsx3

def talk(words):
    # print(words)
    # os.system("say " + words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Govori")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio).lower()
        print("You say " + zadanie)
    except sr.UnknownValueError:
        talk("Idi ot suda Petuh")
        zadanie = command() 
    
    return zadanie

def makeSomething(zadanie):
    if 'open website'.lower() in zadanie:
        talk("Sha otkroyou")
        url = 'https://vk.com/id161119726'
        webbrowser.open(url)
    elif 'stop'.lower() in zadanie:
        talk("chao bombina")
        sys.exit()


talk("Privet, Andrey tu-tu-ru-tu")

while True:
    makeSomething(command())


