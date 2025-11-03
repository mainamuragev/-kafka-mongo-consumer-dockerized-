## 📄 README.md

```markdown
# Kafka-Mongo Consumer Dockerized

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![Last Commit](https://img.shields.io/github/last-commit/mainamuragev/-kafka-mongo-consumer-dockerized-)
![Repo Size](https://img.shields.io/github/repo-size/mainamuragev/-kafka-mongo-consumer-dockerized-)
![Built by MainaMurage](https://img.shields.io/badge/Built%20by-MainaMurage-black)

Real-time employee data pipeline using Kafka, MongoDB, and Docker Compose.  
Streams JSON messages from a Python producer to a Dockerized consumer, ingests into MongoDB, and visualizes Kafka topics with Kafdrop.

---

## 🔧 Stack Overview

- **Kafka + ZooKeeper**: Message broker and coordination
- **MongoDB**: Document storage
- **Python Producer**: Sends employee records to Kafka
- **Python Consumer**: Reads from Kafka and inserts into MongoDB
- **Kafdrop**: Web UI for Kafka topic inspection
- **Docker Compose**: Orchestrates the entire stack

---

## 🚀 Getting Started

### Clone the repo

```bash
git clone https://github.com/mainamuragev/-kafka-mongo-consumer-dockerized-.git
cd employee_streams
```

### Build and launch the stack

```bash
docker compose up -d --build
```

### Activate virtual environment and run the producer

```bash
source venv/bin/activate
python producer.py
```

---

## 📊 Observability

Visit [http://localhost:9000](http://localhost:9000) to inspect Kafka topics via Kafdrop.

---

## 🗃️ MongoDB Validation

Connect to the MongoDB container:

```bash
docker exec -it employee_streams-mongo-1 mongosh
```

Then run:

```js
use employee_db
db.employees.find().pretty()
```

---

## 📁 Project Structure

```
employee_streams/
├── consumer.py              # Kafka consumer that writes to MongoDB
├── producer.py              # Kafka producer that sends employee data
├── data_gen.py              # Optional data generator for testing
├── data.ipynb               # Jupyter notebook for exploration
├── requirements.txt         # Python dependencies
├── Dockerfile.consumer      # Dockerfile for the consumer
├── docker-compose.yml       # Multi-container orchestration
└── venv/                    # Local Python environment (excluded via .gitignore)
```

---

## 📌 Notes

- Ensure port `27017` is free before starting MongoDB container.
- Kafdrop runs on port `9000` (HTTP only).
- MongoDB access control is disabled for local development.

---

## 🪪 License

MIT — feel free to fork, adapt, and build on it.

---

## 💥 Built by MainaMurage

Backend architect. Pipeline whisperer. Container conjurer.  
This repo is part of a growing constellation of real-time data systems — engineered with precision, resilience, and a touch of swagger.
```
