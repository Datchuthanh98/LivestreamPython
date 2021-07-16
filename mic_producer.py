import logging
import pickle
import time
import json
import threading
import pyaudio
import wave
import sys

from kafka import KafkaProducer
CHUNK = 1024
audio = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 20
frames = []

class Producer(threading.Thread):
    daemon = True
    def run(self):
        position = 0
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)

        producer = KafkaProducer(bootstrap_servers='192.168.75.128:6667',
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))





        while (True):
            data = stream.read(CHUNK)
            producer.send('test-events', {
                "data": data.decode('latin-1')
                 })
            position += 1
     

def main():
    threads = [
        Producer(),
    ]
    for t in threads:
        t.start()
    time.sleep(100000)
if __name__ == "__main__":
    main()