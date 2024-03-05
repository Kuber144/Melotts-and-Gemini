from melo.api import TTS
from playsound import playsound

speed = 1.0
device = 'auto'

text = "Hello"
model = TTS(language='EN', device=device)
speaker_ids = model.hps.data.spk2id



output_path = 'en-us.wav'
model.tts_to_file(text, speaker_ids['EN-US'], output_path, speed=speed)


playsound('/home/kuber/Desktop/en-us.wav')