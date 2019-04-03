import sys
from confluent_kafka import Consumer, KafkaError

if len(sys.argv)<5:

    print ("Usage:")
    print ("python3 consumer-parms brokers topic user key ")
    sys.exit()

brokers=sys.argv[1]
topic=sys.argv[2]
user=sys.argv[3]
key=sys.argv[4]


print ("Starting consumer");

# Start consumer
c = Consumer({
    'bootstrap.servers': '$brokers',
    'sasl.mechanisms': 'SCRAM-SHA-512',
    'security.protocol': 'SASL_SSL',
    'sasl.username': '$user',
    'sasl.password': '$key',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['$topic'])
print (c) 

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()