from kafka import KafkaConsumer
from pymongo import MongoClient
import json
import os

# Read connection settings from environment variables
bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

# Kafka setup
consumer = KafkaConsumer(
    'employee',
    bootstrap_servers=[bootstrap_servers],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='employee-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    api_version=(2, 8, 0)
)

# MongoDB setup
mongo_client = MongoClient(mongo_uri)
db = mongo_client['employee_db']
collection = db['employees']

print("Consuming messages and inserting into MongoDB...\n")

for message in consumer:
    print(f"Received: {message.value}")
    collection.insert_one(message.value)