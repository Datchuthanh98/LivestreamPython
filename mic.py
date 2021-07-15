import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 20
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

#start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

stream2 = audio.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True)
print("recording...")
frames = []

while(True):
    data = stream.read(CHUNK)
    stream2.write(data)
print
"finished recording"

# stop Recording
stream.stop_stream()
stream.close()
stream2.stop_stream()
stream2.close()
audio.terminate()

