from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST")

r = redis.Redis(
    host=redis_host,
    port=6379,
    decode_responses=True
)

@app.route('/')
def home():
    count = r.incr("hits")
    return f"Hello from Flask! Visits={count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
