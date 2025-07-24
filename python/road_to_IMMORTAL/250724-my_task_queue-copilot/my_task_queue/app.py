# app.py
from fastapi import FastAPI
from redis import Redis
from rq import Queue
from tasks import send_fake_email

# Initialize FastAPI app
app = FastAPI()

# Connect to Redis and create a queue
redis_conn = Redis(host='localhost', port=6379)
q = Queue(connection=redis_conn)

@app.get("/send-email/{email}")
def trigger_email(email: str):
    # Add the job to the queue
    job = q.enqueue(send_fake_email, email)

    # Respond immediately to the user
    return {
        "message": "Email sending task has been queued.",
        "job_id": job.id
    }
