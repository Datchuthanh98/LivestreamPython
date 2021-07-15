import logging
import time
import json
import threading

from kafka import KafkaConsumer

class Consumer(threading.Thread):
    daemon = True
    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='192.168.75.128:6667',
                                 auto_offset_reset='latest',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        consumer.subscribe(['test-events'])
        for message in consumer:
            print(message.value["meme"])

def main():
    threads = [
        Consumer()
    ]
    for t in threads:
        t.start()
    time.sleep(10)
if __name__ == "__main__":
    main()