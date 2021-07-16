import logging
import time
import json
import threading
import pyaudio
import wave
import sys


from kafka import KafkaConsumer
CHUNK = 1024


# instantiate PyAudio (1)
audio = pyaudio.PyAudio()

# open stream (2)

# audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
#                 channels=wf.getnchannels(),
#                 rate=wf.getframerate(),
#                 output=True)


class Consumer(threading.Thread):
    daemon = True

    def run(self):
        stream = None
        consumer = KafkaConsumer(bootstrap_servers='192.168.75.128:6667',
                                 auto_offset_reset='latest',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        consumer.subscribe(['test-events'])


        for message in consumer:
            print("data")
            if stream == None:
                stream = audio.open(
                    format=message.value["format"],
                    channels=int(message.value["channels"]),
                    rate= int(message.value["rate"]),
                    output = True)
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