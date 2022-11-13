import os
import playsound
import threading
runner = None
def execute(voca,voca_say,listen_and_understand,heard=""):
    voca_say("Do you want me to speak in male or female voice? ")
    heard = listen_and_understand().lower()
    if heard =="female":
        voca_say("switching to female voice")
        voca.voice.setgender(1)
    else:
        voca_say("switching to male voice")
        voca.voice.setgender(0)
