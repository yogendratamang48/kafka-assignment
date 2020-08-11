from kafka import KafkaConsumer, KafkaProducer
import os

TOPIC_NAME = os.environ.get('TOPIC_NAME')
RESULT_TOPIC = os.environ.get('RESULT_TOPIC')
GROUP_NAME = os.environ.get('GROUP_NAME')
TOTAL_PARTITIONS = os.environ.get('TOTAL_PARTITIONS')

BROKER_URL = os.environ.get('BROKER_URL')


consumer = KafkaConsumer(TOPIC_NAME,
                         group_id=GROUP_NAME,
                         value_deserializer=lambda v: int(v.decode('utf-8')),
                         key_deserializer=lambda v: v.decode(),
                         consumer_timeout_ms=4000,
                         auto_offset_reset='earliest'
                        )
collector = []
print(f"Reading data from {TOPIC_NAME}")
for message in consumer:
    collector.append(message.value)

collector = sorted(collector)

# Sending to Another Stream
producer = KafkaProducer(
    bootstrap_servers=BROKER_URL,
    value_serializer=lambda value: str(value).encode()
    )

print(f"Streaming combined data into..{RESULT_TOPIC}")
print(collector)
for element in collector:
    producer.send(RESULT_TOPIC, value=element)
producer.close()

