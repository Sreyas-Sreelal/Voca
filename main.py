import core
import speech_recognition

recongnise_options ={
	"API": "google",
	"energy_threshold": False
}

voice_options ={
	"gender": "female",
	"speech_rate": 140,
}	

ai_options ={
	"learn_file": "voca.aiml",
	"brain_file": "voca.dump",
	"predicates":{
		"name" : "Voca",
		"master": "Sreyas",
		"botmaster": "Sreyas",
		"religion": "atheism",
	}
}

if __name__ == "__main__":
	core.start(recongnise_options,voice_options,ai_options)
