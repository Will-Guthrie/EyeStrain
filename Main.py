import pyaudio
import wave
import sys
import time

# Replace alarm.wav with desired sound effect wav file
wf = wave.open('alarm.wav', 'rb')

# Size of audio chunk to read from wav file
audioChunk = 1024

def alarm(audio, audioStream):
        while len(audio) > 0:
                audioStream.write(audio)
                audio = wf.readframes(audioChunk)
        wf.rewind()

def eyeStrain():
        p = pyaudio.PyAudio()

        # open audio stream with pyaudio
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
        
        audioStart = wf.readframes(audioChunk)

        while True:                
                # Work for 20 minutes (1200 seconds)
                time.sleep(1200)
                alarm(audioStart, stream)

                # Look away for 20 seconds
                time.sleep(20)
                alarm(audioStart, stream)
try:
        eyeStrain()
except KeyboardInterrupt:
        exit()



