from recognize import Recognizer
from ai import AI
from voice import Voice
from speech_recognition import UnknownValueError, RequestError
from commands.cmds import voca_commands
import string


class Core:
    def __init__(self):
        self.voice = Voice()
        self.brain = AI()
        self.recognizer = Recognizer()

    def run(self):
        while True:
            try:
                heard = self.recognizer.listen_and_understand().lower()

                if "shutdown" in heard:
                    self.voice.emit("Ok   I will turn OFF myself")
                    exit()

                for cmd in voca_commands.keys():
                    if heard.startswith(cmd):
                        if heard.strip() == cmd:
                            print("hear")
                            voca_commands[cmd].execute(
                                self.voice.emit, self.recognizer.listen_and_understand)
                        else:
                            print(heard[len(cmd):])
                            voca_commands[cmd].execute(
                                self.voice.emit, self.recognizer.listen_and_understand, heard[len(cmd):])
                        continue

                response = self.brain.generate_response(heard)
                self.voice.emit(response)

            except UnknownValueError:
                #voca_say("What you mean  I dont really understood that")
                continue

            except RequestError:
                self.voice.emit(
                    "Seems like there is an issue with my internet connection")
