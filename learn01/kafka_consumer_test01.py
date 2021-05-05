from confluent_kafka import Consumer, KafkaException
import sys

conf = {'bootstrap.servers': "localhost:9092",
        'group.id': "foo",
        'auto.offset.reset': 'smallest'}
consumer = Consumer(conf)

running = True

def print_assignment(consumer, partitions):
    print('Assignment:', partitions)

def msg_process(msg):
    print("kafka message is : %s" %msg)

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

basic_consume_loop(consumer,["test"])

def shutdown():
    running = False