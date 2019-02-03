import speech_recognition

recognizer = None
API = None

def setup_recogniser(options):
	global recognizer,API
	recognizer = speech_recognition.Recognizer()
	recognizer.dynamic_energy_threshold = options.get("enery_threshod",False)
	if options.get("API","sphinx") == "google":
		API = recognizer.recognize_google
	else:
		API = recognizer.recognize_sphinx

		
def listen_and_understand():
	with speech_recognition.Microphone() as source:
		print("Ears are wide open!!")
		#recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
	
	print("Recognising...")
	recongnize = API(audio)
	print("You said : " + recongnize)

	return recongnize