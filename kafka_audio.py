import logging
import time
import json
import threading

from kafka import KafkaProducer
from kafka import KafkaConsumer


class Producer(threading.Thread):
    daemon = True
    def run(self):
        producer = KafkaProducer(bootstrap_servers='192.168.75.128:6667',
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        while True:
            producer.send('test-events', { "meme": "test1"})
            producer.send('test-events', {"meme": "test2"})
            time.sleep(1)


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
        Producer(),
        Consumer()
    ]
    for t in threads:
        t.start()
    time.sleep(10)
if __name__ == "__main__":
    main()