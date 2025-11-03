from kafka import KafkaProducer
from data_gen import gen
import json, time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8'),
    api_version=(2, 8, 0),  # Avoids version negotiation
    request_timeout_ms=30000,
    retries=5
)

for r in gen(4):
    producer.send("employee", value=r)
    print(f"Sent: {r}")
    time.sleep(30)

producer.flush()