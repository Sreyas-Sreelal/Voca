import pyttsx3

voice_engine = None

def setup_voice(options):
	global voice_engine
	voice_engine = pyttsx3.init()

	voice_engine.setProperty('rate', options.get("speech_rate",150))
	
	voices = voice_engine.getProperty('voices')
	if options.get("gender","male") == "female":
		voice_engine.setProperty('voice', voices[1].id)
	else:
		voice_engine.setProperty('voice', voices[0].id)

def voca_say(text):
	try:
		voice_engine.say(text)
		voice_engine.runAndWait()
	except Exception as e:
		print("Error voca say",str(e))
		#stop_say()

