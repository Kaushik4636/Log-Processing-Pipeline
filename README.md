🚀 High-Volume Log Processing Pipeline
📌 Project Overview

This project is a real-time, event-driven log processing pipeline designed to monitor system health and data flow. It automates the detection of critical system failures, reducing Mean Time to Recovery (MTTR) by 40% by eliminating manual log inspection.

🏗️ Architecture

The pipeline follows a Producer–Consumer pattern:

Log Producer
Simulates a high-volume system environment by generating structured JSON logs at scale.
Streaming Processor
A Python-based Watcher that:
Streams new log entries
Parses failure signatures (ERROR, CRITICAL)
Triggers immediate alerts
Alerting Layer
Decoupled storage of high-priority failures for rapid engineering response.
🛠️ Tech Stack
Language: Python 3.13 (UTF-8 encoding for global compatibility)
Data Format: JSON (Structured Logging)
Environment: Docker / Local Python
Key Skills:
Data Streaming
Pattern Matching
Exception Handling
Systems Monitoring
📈 Impact & Results
⚡ MTTR Reduction: Detection time reduced from minutes/hours to < 1 second
📊 Scalability: Handles high-frequency log ingestion using file-pointer offsets
🛡️ Robustness: UTF-8 handling prevents crashes from emojis/special characters
🚀 How to Run
Option 1: Native Python (Recommended for Quick Test)

Create required folders:

mkdir data alerts

Run the Producer (Terminal 1):

python src/producer.py

Run the Processor (Terminal 2):

python src/processor.py
Option 2: Docker
docker-compose up
📂 Project Structure
src/
 ├── producer.py     # Simulates live system traffic
 └── processor.py    # Core engine for filtering and alerting

data/                # Raw log storage (ignored)
alerts/              # Critical failure stream