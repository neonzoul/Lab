# tasks.py
import time

def send_fake_email(email_address: str):
    """
    A slow function that simulates sending an email.
    """
    print(f"Starting to send email to {email_address}...")
    time.sleep(10)  # Simulate a 10-second delay
    print(f"Email sent to {email_address}!")
    return f"Task complete: Email sent to {email_address}"
