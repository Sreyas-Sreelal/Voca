import aiml
import os
from config import ai_options as options

class AI:
	def __init__(self):
		self.bot_kernel = aiml.Kernel()
		if os.path.exists(options["brain_file"]):
			self.bot_kernel.loadBrain(options["brain_file"])
		else:
			self.bot_kernel.bootstrap(learnFiles=options["learn_file"], commands="load aiml b")
			self.bot_kernel.saveBrain(options["brain_file"])
			
		if options.get("predicates") != None:
			for (keys,value) in options.get("predicates").items():
				self.bot_kernel.setBotPredicate(keys,value)
			
	def generate_response(self,text):
		return self.bot_kernel.respond(text)