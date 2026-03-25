import requests
import json
import time
from kafka import KafkaProducer

API_KEY = "****************"
TOPIC = "stock_data"

# Create Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='127.0.0.1:29092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def fetch_stock_data():
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey={API_KEY}"
    response = requests.get(url)
    return response.json()

while True:
    try:
        data = fetch_stock_data()
        producer.send(TOPIC, value=data)
        print("Data sent to Kafka:", data)
        time.sleep(60)  # API limit safe
    except Exception as e:
        print("Error:", e)
