import wikipedia
from nltk.tokenize import sent_tokenize
def execute(voca,voca_say,listen_and_understand,heard=""):
	if heard == "":
		voca_say("Ok tell me what you want to search in wikipedia")
		heard = listen_and_understand().lower()
	try:
		result = sent_tokenize(wikipedia.summary(heard))[0]
		voca_say(result)
	except wikipedia.exceptions.DisambiguationError:
		voca_say("Disambiguation Error, "+ heard+" can be refered to more than one result, try again with precise details")
	except:
		voca_say("Sorry due to some technical problem i can't search for "+ heard)
	
	