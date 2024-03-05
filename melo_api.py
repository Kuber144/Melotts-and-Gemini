from melo.api import TTS
from playsound import playsound

speed = 1.0
device = 'auto' 

# English 
model = TTS(language='EN', device=device)
speaker_ids = model.hps.data.spk2id
# American accent
output_path = 'en-us.wav'

def generate_tts(res):
	model.tts_to_file(res, speaker_ids['EN-US'], output_path, speed=speed)
	#Replace this path with the path to where your output file will be generated
	playsound('/home/kuber/Desktop/en-us.wav') 