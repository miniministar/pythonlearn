from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}
producer = Producer(conf)
topic = 'test'
for i in range(3):
    key = "key%d" %i
    msg = "msg %d" %i
    print(key, msg)
    producer.produce(topic, key=key, value=msg)

producer.flush()