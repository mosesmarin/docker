import sys
from confluent_kafka import Consumer, KafkaError, TopicPartition, OFFSET_BEGINNING, OFFSET_END


if __name__== '__main__':

    if len(sys.argv)<5:

        print ("Usage:")
        print ("python3 consumer-parms brokers topic user key [beginning]")
        sys.exit()
    
    brokers=sys.argv[1]
    topic=sys.argv[2]
    user=sys.argv[3]
    key=sys.argv[4]
    consumer_offset=''
    if len(sys.argv)==6:
        consumer_offset=sys.argv[5]



    print ("Starting consumer");

    # Start consumer
    c = Consumer({
        'bootstrap.servers': brokers,
        'sasl.mechanisms': 'SCRAM-SHA-512',
        'security.protocol': 'SASL_SSL',
        'sasl.username': user,
        'sasl.password': key,
        'group.id': 'mygroup'
    })

    def my_assign (consumer, partitions):
        #for p in partitions:
            #p.offset=OFFSET_END
        print ('assign', partitions)
        consumer.assign(partitions)

    def my_assign_beginning (consumer, partitions):
        for p in partitions:
            p.offset=OFFSET_BEGINNING
        print ('assign', partitions)
        consumer.assign(partitions)


    if consumer_offset=='beginning':
        c.subscribe([topic], on_assign=my_assign_beginning)
    else:
        c.subscribe([topic], on_assign=my_assign)    
    

    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        print('Received message: {}'.format(msg.value().decode('utf-8')))

    c.close()
    
    