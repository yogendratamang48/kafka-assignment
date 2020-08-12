from kafka import KafkaConsumer, KafkaProducer
import os
from redis_helper import RedisClient

TOPIC_NAME = os.environ.get('TOPIC_NAME')
RESULT_TOPIC = os.environ.get('RESULT_TOPIC')
GROUP_NAME = os.environ.get('GROUP_NAME')
TOTAL_PARTITIONS = os.environ.get('TOTAL_PARTITIONS')


REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT'))
REDIS_DB = int(os.environ.get('REDIS_DB'))
REDIS_LIST_NAME = os.environ.get('REDIS_LIST_NAME')

BROKER_URL = os.environ.get('BROKER_URL')

redis_client = RedisClient(REDIS_HOST, REDIS_PORT, REDIS_DB)

def process_message(msg):
    """saves data to redis list
    """
    # print("Processing inside redis..")
    redis_client.save_to_list(REDIS_LIST_NAME, msg)


if __name__ == '__main__':
    consumer = KafkaConsumer(
                            TOPIC_NAME,
                            bootstrap_servers=BROKER_URL,
                            group_id=GROUP_NAME,
                            value_deserializer=lambda v: int(v.decode('utf-8')),
                            key_deserializer=lambda v: v.decode(),
                            consumer_timeout_ms=4000,
                            auto_offset_reset='earliest'
                            )
    print(f"Reading data from {TOPIC_NAME}")
    for message in consumer:
        process_message(message.value)

    # Sending to Another Stream
    producer = KafkaProducer(
        bootstrap_servers=BROKER_URL,
        # value_serializer=lambda value: str(value).encode()
        )

    print(f"Streaming combined data into..{RESULT_TOPIC}")
    for element in redis_client.retrieve_list(REDIS_LIST_NAME):
        # print(f"Reading from redis: ... {element}")
        producer.send(RESULT_TOPIC, value=element)
    producer.close()

