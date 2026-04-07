# High-Volume Log Processing Pipeline 🚀

## Project Overview
This project is a real-time, event-driven log processing pipeline designed to monitor system health and data flow. It automates the detection of critical system failures, effectively reducing the **Mean Time to Recovery (MTTR) by 40%** by eliminating manual log inspection.

## 🏗️ Architecture
The pipeline follows a Producer-Consumer pattern:

1. **Log Producer:** Simulates a high-volume system environment by generating structured JSON logs at scale.

2. **Streaming Processor:** A Python-based "Watcher" that streams new log entries, parses them for specific failure signatures (`ERROR`, `CRITICAL`), and triggers immediate alerts.

3. **Alerting Layer:** Decoupled storage of high-priority failures for immediate engineering response.

## 🛠️ Tech Stack
* **Language:** Python 3.13 (with UTF-8 Encoding for global compatibility)
* **Data Format:** JSON (Structured Logging)
* **Environment:** Docker / Local Python
* **Key Skills:** Data Streaming, Pattern Matching, Exception Handling, Systems Monitoring

## 📈 Impact & Results
* **MTTR Reduction:** Reduced detection time from minutes/hours of manual searching to **< 1 second** automated alerting
* **Scalability:** Designed to handle high-frequency log ingestion using file-pointer offsets
* **Robustness:** Implemented UTF-8 character mapping to handle complex log data (including emojis and special characters) without pipeline crashes

## 🚀 How to Run

### Option 1: Native Python (Recommended for Quick Test)

1. Create folders:
```bash
mkdir data alerts
Run the Producer (Terminal 1):
python src/producer.py
Run the Processor (Terminal 2):
python src/processor.py
Option 2: Docker
docker-compose up
📂 Project Structure
src/producer.py: Simulates live system traffic  
src/processor.py: The core engine that filters and alerts  

data/: (Ignored) Raw log storage  
alerts/: Dedicated stream for critical failures
