# -*- coding:utf-8 -*-
"""
project: pythonlearn
file: kafka_util
author: admin
create date: 2021/6/6 8:32
description: 
"""
from confluent_kafka import Producer, Consumer, KafkaException, KafkaError
import socket, sys

conf = {'bootstrap.servers':"localhost:9092", "client.id":socket.gethostname()}
producer = Producer(conf)

consumer_conf = {
    'bootstrap.servers': "localhost:9092",
    'group.id': "foo",
    'auto.offset.reset': 'smallest'
}
consumer = Consumer(consumer_conf)
running = True

def print_assignment(consumer, partitions):
    print('Assignment:', partitions)

def shutdown():
    running = False

def basic_consume_loop(consumer, topics):
    try:
        # Subscribe to topics
        consumer.subscribe(topics, on_assign=print_assignment)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                sys.stderr.write('topic: %s partition: [%d] at offset %d with key %s: value: %s\n' %
                                 (msg.topic(), msg.partition(), msg.offset(),
                                  str(msg.key(),'utf-8'), str(msg.value(),'utf-8')) )
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()


def produce_test():
    topic = "test"
    for i in range(3):
        key = "key%d" % i
        msg = "消息%d" % i
        print(key, msg)
        producer.produce(topic, key, msg)
    producer.flush()

if __name__ == '__main__':
    # produce_test()
    basic_consume_loop(consumer, ["test"])
    pass