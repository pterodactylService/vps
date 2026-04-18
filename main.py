import time
from datetime import datetime

def run_forever():
    print("--- The program began its 30-day work ---")
    
    # It runs for about 5.5 hours, then GitHub Actions will restart it.
    start_time = time.time()
    seconds_in_5_hours = 5.5 * 60 * 60 

    while time.time() - start_time < seconds_in_5_hours:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[{now}] The system is active. Running on a free server...")
        
        # Waiting 5 minutes for next check
        time.sleep(300) 

if __name__ == "__main__":
    run_forever()
