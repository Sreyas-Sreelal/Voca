import pyttsx3

voice_engine = None

def setup_voice(options):
	global voice_engine
	voice_engine = pyttsx3.init()

	voice_engine.setProperty('rate', options.get("speech_rate",150))
	
	voices = voice_engine.getProperty('voices')
	try:
		if options.get("gender","male") == "female":
			gender = list(filter(lambda v:v.gender == "female",voices))[0]
			voice_engine.setProperty('voice', gender.id)
		else:
			gender = list(filter(lambda v:v.gender == "male",voices))[0]
			voice_engine.setProperty('voice', gender.id)
	except IndexError:
		print("Warning cannot set gender properly!")

def voca_say(text):
	try:
		voice_engine.say(text)
		voice_engine.runAndWait()
	except Exception as e:
		print("Error voca say",str(e))
		#stop_say()

