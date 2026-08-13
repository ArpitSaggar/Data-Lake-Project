import json
import pandas as pd
from pathlib import Path
from kafka import KafkaProducer

# ----------------------------
# Kafka Producer Configuration
# ----------------------------
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# ----------------------------
# Locate CSV File
# ----------------------------
csv_path = (
    Path(__file__).resolve().parent.parent
    / "data_generator"
    / "clickstream_data.csv"
)

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_csv(csv_path)

print(f"Loaded {len(df)} records.")

# ----------------------------
# Stream Data to Kafka
# ----------------------------
for i, row in df.iterrows():
    producer.send("clickstream", row.to_dict())

    if i % 1000 == 0:
        producer.flush()
        print(f"Sent {i} records")

# ----------------------------
# Finish
# ----------------------------
producer.flush()
producer.close()

print("Finished streaming data.")