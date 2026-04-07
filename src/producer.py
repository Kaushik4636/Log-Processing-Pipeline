import json
import time
import random
from datetime import datetime

LOG_FILE = "data/system.log"

LOG_LEVELS = ["INFO", "INFO", "INFO", "WARNING", "ERROR", "CRITICAL"]
MESSAGES = [
    "User login successful",
    "API request received",
    "Database connection healthy",
    "Schema mismatch detected",
    "Connection timeout",
    "Disk space running low",
    "Memory spike detected"
]

def generate_logs():
    print("🚀 Starting Log Producer (Simulating high-volume traffic)...")
    while True:
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "level": random.choice(LOG_LEVELS),
            "message": random.choice(MESSAGES),
            "service": "auth-service"
        }
        
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        
        # Random sleep to simulate real-time traffic
        time.sleep(random.uniform(0.1, 1.0))

if __name__ == "__main__":
    generate_logs()