"""
redis_helper.py 


"""
from datetime import datetime
import redis

BATCH_SIZE = 100
class RedisClient():
    def __init__(self, host, port, db):
        self.r = redis.Redis(host=host, port=port, db=db)
        self.r.set('foo', 'bar')    
        # self.r.set('foo', 'bar')

    def save_to_list(self, list_name, value):
        """
        pushes data to list
        """
        self.r.rpush(list_name, value)
        # print(f"Pushed to {list_name}")

    
    def retrieve_list(self, list_name):
        """
        returns data from list
        """
        batch_counter = 0
        while True:
            start_index = batch_counter * BATCH_SIZE
            end_index = start_index + BATCH_SIZE
            for index, element in enumerate(self.r.sort(list_name, start_index, end_index)):
                yield element
            # Termination condition
            # print(f"Index: {index}")
            batch_counter += 1
            if index < (BATCH_SIZE - 1):
                break


