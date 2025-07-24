#!/usr/bin/env python3
import redis
from rq import SimpleWorker, Queue
import sys
import os

# Make sure we can import tasks
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    # Import here to make sure it's available
    import tasks
    
    # Connect to Redis
    redis_conn = redis.Redis(host='localhost', port=6379)
    
    # Create a queue
    q = Queue(connection=redis_conn)
    
    # Create and start the worker (using SimpleWorker for Windows compatibility)
    worker = SimpleWorker([q], connection=redis_conn)
    print("Starting worker...")
    worker.work()
