import aiml
import os

bot_kernel = None

def setup_ai(options):
	global bot_kernel
	bot_kernel = aiml.Kernel()
	
	if os.path.exists(options["brain_file"]):
		bot_kernel.loadBrain(options["brain_file"])
	else:
		bot_kernel.bootstrap(learnFiles=options["learn_file"], commands="load aiml b")
		bot_kernel.saveBrain(options["brain_file"])
		
	if options.get("predicates") != None:
		for (keys,value) in options.get("predicates").items():
			bot_kernel.setBotPredicate(keys,value)
		
def generate_response(text):
	return bot_kernel.respond(text)