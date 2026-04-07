import json
import time
import os

LOG_FILE = "data/system.log"
ALERT_FILE = "alerts/pipeline_failures.txt"

def process_logs():
    print("👀 Watcher Active: Scanning for pipeline failures...")
    
    # Ensure folders exist
    os.makedirs("alerts", exist_ok=True)

    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'a').close()

    # Added encoding="utf-8" here
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        f.seek(0, 2)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            
            try:
                log_entry = json.loads(line)
                if log_entry["level"] in ["ERROR", "CRITICAL"]:
                    send_alert(log_entry)
            except json.JSONDecodeError:
                continue

def send_alert(entry):
    alert_msg = f"🚨 ALERT | {entry['timestamp']} | Level: {entry['level']} | Message: {entry['message']}\n"
    print(alert_msg.strip())
    
    # Added encoding="utf-8" here to fix the crash
    with open(ALERT_FILE, "a", encoding="utf-8") as f:
        f.write(alert_msg)

if __name__ == "__main__":
    process_logs()