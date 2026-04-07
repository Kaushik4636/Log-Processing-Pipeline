# High-Volume Log Processing Pipeline 🚀

## 📝 Project Overview
This project is a real-time, event-driven log monitoring and alerting system. It simulates a high-traffic production environment where system logs are continuously generated and must be parsed instantly to identify failures.

By automating the detection of CRITICAL and ERROR events, this pipeline aims to reduce the Mean Time to Recovery (MTTR) by 40% by eliminating the need for manual log tailing and grep-based debugging.

## 🏗️ Architecture
The pipeline follows a Producer-Consumer pattern:

- **Log Producer:** A Python script generating high-frequency JSON-structured logs (Success, Warning, Error, Critical).

- **Streaming Processor:** A robust "Watcher" that tracks the log file using file-pointer offsets to process only new data in real-time.

- **Alerting Layer:** A dedicated alerting stream that isolates failures for immediate engineering intervention.

## 🛠️ Tech Stack
- **Language:** Python 3.13  
- **Data Format:** JSON (Structured Logging)  
- **Containerization:** Docker & Docker Compose  
- **Environment:** Cross-platform (Windows/Linux/macOS) with UTF-8 support  

## 📈 Key Features & Performance
- **Sub-second Latency:** Alerts are generated within milliseconds of the error occurring  
- **Efficient I/O:** Uses file-pointer tracking (f.seek) to ensure low CPU and memory overhead, even as log files grow to gigabyte scale  
- **Fault Tolerance:** Built-in UTF-8 encoding handling to prevent pipeline crashes from non-standard characters (emojis, symbols)  
- **MTTR Optimization:** Reduces "Time to Discovery" from minutes to milliseconds  

## 📂 Project Structure

## 📂 Project Structure

```text
log-processor-pipeline/
├── data/               # Simulated raw log storage
├── alerts/             # Real-time failure alerts
├── src/
│   ├── producer.py     # Generates high-volume traffic
│   └── processor.py    # The core Log Parser engine
├── docker-compose.yml  # Container orchestration
└── .gitignore          # Prevents data leakage

## 🚀 How to Run

### Prerequisite
Python 3.x installed OR Docker Desktop installed.

### Setup
Clone the repository:

git clone https://github.com/YOUR_USERNAME/log-processor-pipeline.git

cd log-processor-pipeline


Create the necessary directories:

mkdir data alerts


### Running Locally (Native Python)

Start the Producer (Terminal 1):

python src/producer.py


Start the Processor (Terminal 2):

python src/processor.py


### Running with Docker

docker-compose up


## 🛡️ Security & Best Practices
- **Data Privacy:** All generated logs and alerts are excluded from version control via .gitignore to prevent sensitive data exposure  
- **Decoupling:** The producer and processor run independently, simulating a distributed microservices environment  
