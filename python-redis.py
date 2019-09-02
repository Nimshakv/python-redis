import redis
import json
import datetime as dt


_redis_ip = "localhost"
_redis_port = 6379
_key = "sample"


# connecting to redis
try:
    redis = redis.StrictRedis(host=_redis_ip, port=_redis_port)
except Exception as e:
    raise Exception(f"Error connecting to redis server {str(e)}")


# setting json value to redis
_data = {
         "time_stamp": dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d %H:%M:%S.%f'),
         "value": "sample"
        }
try:
    redis.set(_key, json.dumps(_data))
except Exception as e:
    raise e


# getting json value from redis
try:
    _value = redis.get(_key)
    _value_dict = json.loads(_value)
except Exception as e:
    print("exception")
    raise e

