import pyttsx3
import os
from get_answer import Fetcher

class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("you haven't told me your name yet ?")
            else:
                self.respond("My name is Bearisk. How are you ?")

        else:
            f = Fetcher("https://www.google.com/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)



    def respond(self, response):
        engine = pyttsx3.init()
        print(response)
        engine.say("say'" + response +"'")
        engine.runAndWait()