"""
redis_helper.py 


"""
from datetime import datetime
import redis


class RedisClient():
    def __init__(self, host, port, db):
        pool = redis.ConnectionPool(host=host, port=port, db=db)
        self.conn = redis.Redis(connection_pool = pool)

    def save_to_list(self, value, list_name):
        """
        pushes data to list
        """
        self.conn.rpush(list_name, value)
        # print(f"Pushed to {list_name}")

    
    def retrieve_list(self, list_name):
        """
        returns data from list
        """
        for element in self.conn.sort(list_name):
            yield element

