import os
import playsound
import threading
runner = None
def execute(voca,voca_say,listen_and_understand,heard=""):
	global runner
	if heard == "":
		voca_say("Ok tell me what you want to play")
		heard = listen_and_understand()
	os.system('youtube-dl ytsearch1:"'+heard+'" --extract-audio --audio-format mp3 --output temp.mp3')
	runner = threading.Timer(1,playsound.playsound,["temp.mp3"])
"""
options.Path,
	`ytsearch1:"`+options.TrackName+`"`,
	"--extract-audio",
	"--audio-format",
	options.AudioFormat,
	"--output",
	audioData.Fulltitle+"."+options.AudioFormat,
"""

