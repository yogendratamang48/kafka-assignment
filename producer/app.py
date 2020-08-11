from kafka import KafkaProducer
import random
import os

TOPIC_NAME = os.environ.get('TOPIC_NAME')
TOTAL_PARTITIONS = int(os.environ.get('TOTAL_PARTITIONS'))
BROKER_URL = os.environ.get('BROKER_URL')



def random_sorted_integers(size):
    return sorted([random.randint(1, 10) for _ in range(0, size)])



if __name__ == '__main__':
    producer = KafkaProducer(
    bootstrap_servers=BROKER_URL,
    value_serializer=lambda value: str(value).encode(),
    key_serializer=lambda value: value.encode()
    )
    for i in range(0, TOTAL_PARTITIONS):
        key_name = f"P-{i+1}"
        random_list = random_sorted_integers(random.randint(6, 18))
        print(key_name)
        for data in random_list:
            producer.send(TOPIC_NAME, key=key_name, value=data)
    
    print(f"Producer Sent data...Topic: {TOPIC_NAME}")
    producer.flush()

