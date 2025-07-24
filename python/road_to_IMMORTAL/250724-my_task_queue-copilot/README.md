# Task Queue System - Quick Start Guide

This project demonstrates how to build a simple task queue system using FastAPI, Redis, and RQ (Redis Queue).

## Files Created

-   `tasks.py` - Contains the slow task function (simulated email sending)
-   `app.py` - FastAPI web server that queues tasks
-   `test_system.py` - Script to test the system
-   `redis_setup.md` - Instructions for setting up Redis

## Prerequisites

1. **Python Environment**: ✅ Already configured with virtual environment
2. **Packages Installed**: ✅ fastapi, uvicorn, redis, rq, requests
3. **Redis Server**: ⚠️ You need to set up Redis (see redis_setup.md)

## Quick Start (assuming Redis is running)

### Terminal 1 - Start the RQ Worker

```bash
# Navigate to project directory
cd "../Learn/_lab/_python/250724-my_task_queue"

# Activate virtual environment (if not already active)
.\.venv\Scripts\activate

# Start the worker
rq worker
```

### Terminal 2 - Start the FastAPI Server

```bash
# In a new terminal, navigate to project directory
cd "./Coding-Area/Learn/_lab/_python/250724-my_task_queue"

# Activate virtual environment (if not already active)
.\.venv\Scripts\activate

# Start the web server
uvicorn app:app --reload
```

### Terminal 3 - Test the System

```bash
# In a third terminal, run the test script
cd "./Coding-Area/Learn/_lab/_python/250724-my_task_queue"
.\.venv\Scripts\activate
python test_system.py
```

Or open your browser and go to: `http://127.0.0.1:8000/send-email/moss@example.com`

## What Should Happen

1. The web browser/test script gets an **instant response** (< 1 second)
2. The response includes a message: "Email sending task has been queued"
3. In Terminal 1 (worker), you'll see it pick up the job and process it for 10 seconds
4. After 10 seconds, the worker prints "Email sent!"

## Troubleshooting

-   If you get connection errors, make sure Redis is running on port 6379
-   If the worker doesn't start, check that Redis is accessible
-   If the web server doesn't start, make sure port 8000 is available

## Next Steps

-   Modify the `send_fake_email` function to do actual work
-   Add job status checking endpoints
-   Implement job retries and error handling
-   Add monitoring and logging
