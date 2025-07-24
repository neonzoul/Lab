# test_system.py
import requests
import time

def test_email_endpoint():
    """Test the email endpoint to see if it responds quickly"""
    email = "test@example.com"
    url = f"http://127.0.0.1:8000/send-email/{email}"
    
    print(f"Testing endpoint: {url}")
    start_time = time.time()
    
    try:
        response = requests.get(url)
        end_time = time.time()
        
        print(f"Response time: {end_time - start_time:.2f} seconds")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if end_time - start_time < 2:
            print("✅ SUCCESS: Response was fast (< 2 seconds)")
        else:
            print("❌ FAIL: Response was too slow")
            
    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Could not connect to the server. Make sure the FastAPI server is running.")
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    test_email_endpoint()
