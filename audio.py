import speech_recognition as sr

from playsound import playsound
import pyttsx3

from commands import Commander

running = True

def say(text):
    engine = pyttsx3.init()
    engine.say('say' + text)
    engine.runAndWait()

playsound('audio/done-for-you-612.mp3')

r = sr.Recognizer()
cmd = Commander()

def initSpeech():
    print("Listening....")

    playsound('audio/capisci.mp3')

    with sr.Microphone() as source:
        print("Say Somenthing")
        audio = r.listen(source)


    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you, bro.")
    print("Your command:")
    print(command)
    if command in ["quit", "exit", "bye", "goodbye"]:
        global running
        running = False
    cmd.discover(command)

    #say('you said: ' + command)

while running == True:
    initSpeech()

