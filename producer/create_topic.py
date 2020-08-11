"""
creates topic
"""
from kafka.admin import KafkaAdminClient, NewTopic
import os

BROKER_URL = os.environ.get('BROKER_URL')
TOPIC_NAME = os.environ.get('TOPIC_NAME')
RESULT_TOPIC = os.environ.get('RESULT_TOPIC')
CLIENT_ID = os.environ.get('CLIENT_ID')
TOTAL_PARTITIONS = int(os.environ.get('TOTAL_PARTITIONS'))

try:
    admin_client = KafkaAdminClient(
        bootstrap_servers=BROKER_URL, 
        client_id=CLIENT_ID
    )

    topic_list = []
    topic_list.append(NewTopic(name=TOPIC_NAME, num_partitions=TOTAL_PARTITIONS, replication_factor=1))
    topic_list.append(NewTopic(name=RESULT_TOPIC, num_partitions=1, replication_factor=1))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)
    print("Topic Creation complete...")
except Exception as e:
    print(e)