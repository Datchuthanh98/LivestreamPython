import logging
import pickle
import time
import json
import threading
import pyaudio
import wave
import sys

from kafka import KafkaProducer
audio = pyaudio.PyAudio()

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 10240 *3
RECORD_SECONDS = 20

class Producer(threading.Thread):
    daemon = True
    def run(self):
        position = 0
        producer = KafkaProducer(bootstrap_servers='192.168.75.128:6667',
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        while True:
                wf = wave.open("testt"+".wav", "rb")
                data = wf.readframes(CHUNK)
                while len(data) > 0:
                 print(position)

                 producer.send('test-events', {
                     "position":position,
                     "data": data.decode('latin-1'),
                     "format":audio.get_format_from_width(wf.getsampwidth()),
                     "channels": wf.getnchannels(),
                     "rate":wf.getframerate()})

                 data = wf.readframes(CHUNK)
                 position += 1
                 # time.sleep(1)

def main():
    threads = [
        Producer(),
    ]
    for t in threads:
        t.start()
    time.sleep(100000)
if __name__ == "__main__":
    main()