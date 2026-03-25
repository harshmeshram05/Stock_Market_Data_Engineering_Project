import json
import boto3
from kafka import KafkaConsumer
from datetime import datetime

# Kafka Consumer
consumer = KafkaConsumer(
    'stock_data',
    bootstrap_servers='127.0.0.1:29092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# S3 Client
s3 = boto3.client('s3')

BUCKET_NAME = 'stock-data-raw-harsh'

for message in consumer:
    data = message.value

    # Create unique file name
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name = f"stock_data/{timestamp}.json"

    # Upload to S3
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=json.dumps(data)
    )

    print(f"Uploaded to S3: {file_name}")