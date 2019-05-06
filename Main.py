import pyaudio
import wave
import sys
import time

# Size of audio chunk to read from wav file
audioChunk = 1024

def eyeStrain():
	# Replace alarm.wav with desired sound effect
	wf = wave.open('alarm.wav', 'rb')
	p = pyaudio.PyAudio()

	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True)

	audioData = wf.readframes(audioChunk)


	while True:
		# Work for 20 minutes (1200 seconds)
		time.sleep(1)

		# Play alarm
		while len(audioData) > 0:
			stream.write(audioData)
			audioData = wf.readframes(audioChunk)
			stream.write(audioData)

		# Look away for 20 seconds
		time.sleep(2)

		# Play alarm
		while len(audioData) > 0:
			stream.write(audioData)
			audioData = wf.readframes(audioChunk)
			stream.write(audioData)

try:
	eyeStrain()
except KeyboardInterrupt:
	exit()



