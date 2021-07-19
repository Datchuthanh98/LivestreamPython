import logging
import time
import json
import threading
import pyaudio

from kafka import KafkaConsumer

from DataModel import DataModel
from MyCustomeArray import MyCustomeArray

CHUNK = 10240

# instantiate PyAudio (1)
audio = pyaudio.PyAudio()
myArray = MyCustomeArray();
# open stream (2)

class Consumer(threading.Thread):
    daemon = True
    def run(self):
        stream = None
        consumer = KafkaConsumer(bootstrap_servers='192.168.75.128:6667',
                                 auto_offset_reset='latest',
                                 consumer_timeout_ms=1000,
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        consumer.subscribe(['test-events'])


        for message in consumer:
            data_format = message.value["format"]
            data_channels = int(message.value["channels"])
            data_rate = int(message.value["rate"])
            data_bytes = message.value["data"].encode("latin-1","strict")
            data_position = int(message.value["position"])
            data_model = DataModel(data_bytes,data_format,data_channels,data_rate,data_position)

            myArray.add(data_model)
            take_model = myArray.take()

            if stream == None:
                if take_model != None:
                    stream = audio.open(
                        format=take_model.format,
                        channels=take_model.channels,
                        rate=take_model.rate,
                        output=True)

            if take_model != None:
                print(take_model.position)
                stream.write(take_model.bytes)
            else:
                 print("get pkg none")
            # time.sleep(1./100)

            # stream.stop_stream()
            # stream.close()
            # audio.terminate()

def main():
    threads = [
        Consumer(),
    ]
    for t in threads:
        t.start()
    time.sleep(100000)
if __name__ == "__main__":
    main()