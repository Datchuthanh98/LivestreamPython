import logging
import time
import json
import threading
import pyaudio
import wave
import sys


from kafka import KafkaConsumer


# instantiate PyAudio (1)
audio = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 20

class Consumer(threading.Thread):
    daemon = True

    def run(self):
        stream = audio.open(format=FORMAT,
                             channels=CHANNELS,
                             rate=RATE,
                             output=True)

        consumer = KafkaConsumer(bootstrap_servers='192.168.75.128:6667',
                                 auto_offset_reset='latest',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        consumer.subscribe(['test-events'])


        for message in consumer:
            stream.write(message.value["data"].encode("latin-1","strict"))

        stream.stop_stream()
        stream.close()
        audio.terminate()

def main():
    threads = [
        Consumer()
    ]
    for t in threads:
        t.start()
    time.sleep(100000)
if __name__ == "__main__":
    main()