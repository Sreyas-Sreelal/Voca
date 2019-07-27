import pyttsx3
from config import voice_options as options


class Voice:
    def __init__(self):
        self.voice_engine = pyttsx3.init()
        self.voice_engine.setProperty('rate', options.get("speech_rate", 150))

        voices = self.voice_engine.getProperty('voices')
        try:
            if options.get("gender", "male") == "female":
                gender = list(
                    filter(lambda v: v.gender == "female", voices))[0]
                self.voice_engine.setProperty('voice', gender.id)
            else:
                gender = list(filter(lambda v: v.gender == "male", voices))[0]
                self.voice_engine.setProperty('voice', gender.id)

        except IndexError:
            print("Warning cannot set gender properly!")

    def emit(self, text):
        try:
            self.voice_engine.say(text)
            self.voice_engine.runAndWait()
        except Exception as e:
            print("Error cant emit sound : ", str(e))
            # stop_say()
