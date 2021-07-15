import pyaudio
import wave
import sys

CHUNK = 1024

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s bai3.wav" % sys.argv[0])
    # sys.exit(-1)

wf = wave.open("bai3.wav","rb")

# instantiate PyAudio (1)
audio = pyaudio.PyAudio()

# open stream (2)
stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# read data
data = wf.readframes(CHUNK)

# play stream (3)
while len(data) > 0:
    print(data)
    stream.write(data)
    data = wf.readframes(CHUNK)

# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
audio.terminate()