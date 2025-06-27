import redis
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Use your own Redis host/port if needed
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

BOOKS_CACHE_KEY = "books_cache"

def get_cached_books():
    try:
        cached = r.get(BOOKS_CACHE_KEY)
        if cached:
            return json.loads(cached)
    except redis.exceptions.RedisError as e:
        print(f"Redis error (GET): {e}")
    return None

def set_cached_books(books):
    try:
        r.set(BOOKS_CACHE_KEY, json.dumps(books), ex=60)  # expire in 60s
    except redis.exceptions.RedisError as e:
        print(f"Redis error (SET): {e}")
