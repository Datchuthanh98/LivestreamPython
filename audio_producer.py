import logging
import time
import json
import threading

from kafka import KafkaProducer


class Producer(threading.Thread):
    daemon = True
    def run(self):
        producer = KafkaProducer(bootstrap_servers='192.168.75.128:6667',
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        while True:
            producer.send('test-events', { "meme": "test1"})
            producer.send('test-events', {"meme": "test2"})
            time.sleep(1)

def main():
    threads = [
        Producer(),
    ]
    for t in threads:
        t.start()
    time.sleep(10)
if __name__ == "__main__":
    main()