import pyttsx3
from config import voice_options as options


class Voice:
    def __init__(self):
        self.voice_engine = pyttsx3.init()
        self.voice_engine.setProperty('rate', options.get("speech_rate", 150))

        voices = self.voice_engine.getProperty('voices')
        try:
            if options.get("gender", "male") == "female":
                self.voice_engine.setProperty('voice', voices[1].id)
            else:
                self.voice_engine.setProperty('voice', voices[0].id)

        except IndexError:
            print("Warning cannot set gender properly!")

    def emit(self, text):
        try:
            self.voice_engine.say(text)
            self.voice_engine.runAndWait()
        except Exception as e:
            print("Error cant emit sound : ", str(e))
            # stop_say()
    def setgender(self,genderid):
        voices = self.voice_engine.getProperty('voices')
        self.voice_engine.setProperty('voice', voices[genderid].id)

