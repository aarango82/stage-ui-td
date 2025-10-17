# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.
import openai
from openai import OpenAI
import simplejson as json

def onValueChange(par, prev):
	# use par.eval() to get current value
	return

# Called at end of frame with complete list of individual parameter changes.
# The changes are a list of named tuples, where each tuple is (Par, previous value)
def onValuesChanged(changes):
	for c in changes:
		# use par.eval() to get current value
		par = c.par
		prev = c.prev
	return

def onPulse(par):
	if par.name == 'Sendrequest':
		SubmitRequest()
	return
	
def SubmitRequest(): 
	
	AUDIO_FILE_PATH = me.parent.par.Filepath
	
	client = OpenAI(
		api_key=op('text_apiKey').text
	)

	
	audio_file= open(f"{AUDIO_FILE_PATH}", "rb")
	transcription = client.audio.transcriptions.create(
	model="whisper-1", 
	file=audio_file
	)
	op('text_response2').text = transcription.text

	return
'''
def onExpressionChange(par, val, prev):
	return

def onExportChange(par, val, prev):
	return

def onEnableChange(par, val, prev):
	return

def onModeChange(par, val, prev):
	return
'''
