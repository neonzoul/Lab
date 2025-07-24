# Task Queue System with FastAPI and Redis

A demonstration of asynchronous task processing using FastAPI, Redis, and RQ (Redis Queue). This project shows how to build a responsive web API that can handle slow operations without blocking user requests.

## 🎯 Project Overview

This system implements the classic **Producer-Consumer** pattern for handling time-consuming tasks:

-   **Producer**: FastAPI web server that receives requests and queues tasks
-   **Queue**: Redis acts as the message broker
-   **Consumer**: Background worker processes that execute tasks

## � Project Origin & Purpose

### **Training Foundation**

This project originates from my **Python training journey**, specifically designed to master the core engine concepts for the **AutomateOS project**. The primary focus is on **Asynchronous Programming** - a critical skill for building scalable automation platforms.

### **Development Process**

-   **📋 Problem Design**: The assignment and requirements were brainstormed and created through collaboration with **Gemini 2.5 Pro**, ensuring comprehensive coverage of async programming concepts
-   **🤖 Implementation**: Fully implemented using **GitHub Copilot Agent Mode** with **Claude Sonnet 4** model, showcasing modern AI-assisted development workflows
-   **🎯 Learning Goal**: Understanding asynchronous task processing, message queues, and non-blocking architecture patterns essential for automation systems

### **Connection to AutomateOS**

This task queue system serves as the **foundational training** for the larger AutomateOS project, where similar asynchronous patterns will be used to:

-   Process automation workflows in the background
-   Handle webhook triggers without blocking API responses
-   Execute multiple automation tasks concurrently
-   Ensure scalable and responsive automation platform performance

## �🏗️ Architecture

```
[User Request] → [FastAPI] → [Redis Queue] → [Worker Process]
      ↓              ↓             ↓              ↓
   Instant        Enqueue      Store Job      Process Task
   Response       Task         Message        (10 seconds)
```

## 🚀 Features

-   **Instant API Response**: Web server responds immediately without waiting for task completion
-   **Background Processing**: Time-consuming tasks run in separate worker processes
-   **Scalable**: Can handle multiple requests while tasks process in parallel
-   **Windows Compatible**: Uses SimpleWorker for Windows environment compatibility
-   **Real-time Monitoring**: Worker logs show task processing in real-time

## 📁 Project Structure

```
my_task_queue/
├── app.py          # FastAPI web server (Producer)
├── worker.py       # Background worker (Consumer)
├── tasks.py        # Task definitions
└── README.md       # This file
```

## 🛠️ Installation & Setup

### Prerequisites

-   Python 3.7+
-   Docker (for Redis)
-   Git

### 1. Clone the Repository

```bash
git clone <repository-url>
cd my_task_queue
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install fastapi "uvicorn[standard]" redis rq
```

### 4. Start Redis Server

```bash
docker run -d -p 6379:6379 redis
```

## 🚀 Running the System

### Step 1: Start the Worker

In your first terminal:

```bash
cd my_task_queue
python -c "
import redis
from rq import SimpleWorker, Queue
import sys
sys.path.insert(0, r'F:\\path\\to\\your\\project\\my_task_queue')
import tasks
redis_conn = redis.Redis(host='localhost', port=6379)
q = Queue(connection=redis_conn)
worker = SimpleWorker([q], connection=redis_conn)
print('Starting worker...')
worker.work()
"
```

### Step 2: Start the Web Server

In your second terminal:

```bash
cd my_task_queue
python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

### Step 3: Test the System

Open your browser or use curl:

```bash
# Send an email task
curl "http://127.0.0.1:8000/send-email/user@example.com"

# Response (immediate):
{
  "message": "Email sending task has been queued.",
  "job_id": "abc123-def456-ghi789"
}
```

## 📝 Code Components

### `app.py` - Web Server (Producer)

```python
from fastapi import FastAPI
from redis import Redis
from rq import Queue
from tasks import send_fake_email

app = FastAPI()
redis_conn = Redis(host='localhost', port=6379)
q = Queue(connection=redis_conn)

@app.get("/send-email/{email}")
def trigger_email(email: str):
    job = q.enqueue(send_fake_email, email)
    return {
        "message": "Email sending task has been queued.",
        "job_id": job.id
    }
```

### `tasks.py` - Task Definitions

```python
import time

def send_fake_email(email_address: str):
    """Simulates sending an email with a 10-second delay"""
    print(f"Starting to send email to {email_address}...")
    time.sleep(10)  # Simulate slow operation
    print(f"Email sent to {email_address}!")
    return f"Task complete: Email sent to {email_address}"
```

### `worker.py` - Background Worker (Consumer)

```python
import redis
from rq import SimpleWorker, Queue
import sys
import os

# Import tasks module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tasks

# Connect to Redis and start worker
redis_conn = redis.Redis(host='localhost', port=6379)
q = Queue(connection=redis_conn)
worker = SimpleWorker([q], connection=redis_conn)
worker.work()
```

## 🔍 How It Works

1. **User Request**: Browser/client sends GET request to `/send-email/{email}`
2. **Instant Response**: FastAPI immediately enqueues the task and returns a job ID
3. **Background Processing**: Worker picks up the job from Redis queue
4. **Task Execution**: Worker runs the slow `send_fake_email` function (10 seconds)
5. **Completion**: Task completes in background while server remains responsive

## 🎯 Key Benefits

-   **No Blocking**: Web server never waits for slow operations
-   **User Experience**: Users get instant feedback, no long loading times
-   **Scalability**: Can handle many requests while tasks process separately
-   **Reliability**: Redis persists jobs even if workers restart
-   **Monitoring**: Real-time visibility into task processing

## 🐛 Troubleshooting

### Redis Connection Issues

```bash
# Check if Redis is running
docker ps

# Restart Redis if needed
docker run -d -p 6379:6379 redis
```

### Import Errors

-   Ensure you're in the correct directory
-   Check that all files are in the same folder
-   Verify Python path is set correctly

### Worker Not Processing Jobs

-   Confirm worker is running and connected to Redis
-   Check for import errors in worker terminal
-   Verify Redis is accessible on localhost:6379

## 📚 Learning Objectives

This project demonstrates:

-   **Asynchronous Task Processing**
-   **Producer-Consumer Pattern**
-   **Message Queue Architecture**
-   **FastAPI Web Development**
-   **Redis Integration**
-   **Background Job Processing**

## 🤖 AI-Assisted Development Process

### **Collaborative Development Approach**

This project showcases a modern AI-assisted development workflow:

1. **📋 Requirements & Design Phase**

    - Problem brainstorming and assignment creation with **Gemini 2.5 Pro**
    - Comprehensive requirement analysis for asynchronous programming concepts
    - Educational goal alignment with AutomateOS core engine training

2. **🛠️ Implementation Phase**

    - Full code implementation using **GitHub Copilot Agent Mode**
    - Powered by **Claude Sonnet 4** model for advanced code generation
    - Real-time problem-solving and debugging assistance

3. **🎯 Training Outcome**
    - Hands-on experience with production-ready async patterns
    - Foundation for building scalable automation platforms
    - Bridge between learning concepts and real-world application

This demonstrates how AI tools can accelerate learning and development while maintaining code quality and best practices.

## 📈 Next Steps

To extend this system, consider:

-   Adding job status endpoints (`/job/{job_id}/status`)
-   Implementing job result storage
-   Adding job retry mechanisms
-   Creating a web dashboard for monitoring
-   Setting up multiple worker processes
-   Adding job priority levels
-   Implementing job scheduling

## 📄 License

This project is for educational purposes and demonstrates modern task queue patterns in Python web applications.

---

**Built with ❤️ using FastAPI, Redis, and RQ**
