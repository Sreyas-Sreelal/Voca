import speech_recognition
from config import recongnise_options as options


class Recognizer:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.recognizer.dynamic_energy_threshold = options.get(
            "enery_threshod", False)
        if options.get("API", "sphinx") == "google":
            self.api = self.recognizer.recognize_google
        else:
            self.api = self.recognizer.recognize_sphinx

    def listen_and_understand(self):
        with speech_recognition.Microphone() as source:
            print("Ears are wide open!!")
            # self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        print("Recognising...")
        recongnize = self.api(audio)
        print("You said : " + recongnize)

        return recongnize
