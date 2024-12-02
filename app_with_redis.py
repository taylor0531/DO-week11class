#app_with_redis.py
from flask import Flask
import os
import redis

app = Flask(__name__)

# Connect to the Redis service
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def home():
    # Increment the counter
    counter = redis_client.incr("visit_counter")
    config_value = os.getenv("CONFIG_VALUE", "Default Config")
    return f"""
    <h1>Flask App with Config: {config_value}</h1>
    <p>Page visits: {counter}</p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
