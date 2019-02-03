from recongnize import setup_recogniser,listen_and_understand
from ai import setup_ai,generate_response
from voice import setup_voice,voca_say
from speech_recognition import UnknownValueError,RequestError 
from commands.cmds import voca_commands
import re
import string

def start(recongnise_options,voice_options,ai_options):
	setup_recogniser(recongnise_options)
	setup_voice(voice_options)
	setup_ai(ai_options)

	while True:
		try:
			heard = listen_and_understand().lower()
			
			if "shutdown" in heard:
				voca_say("Ok   I will turn OFF myself")
				exit()
			
			for cmd in voca_commands.keys():
				if heard.startswith(cmd):
					if heard.strip() == cmd:
						print("hear")
						voca_commands[cmd].execute(voca_say,listen_and_understand)
					else:
						print(heard[len(cmd):])
						voca_commands[cmd].execute(voca_say,listen_and_understand,heard[len(cmd):])
					continue

			response = generate_response(heard)
			voca_say(response)

		except UnknownValueError:
			#voca_say("What you mean  I dont really understood that")
			continue
		
		except RequestError:
			voca_say("Seems like there is an issue with my internet connection")
			