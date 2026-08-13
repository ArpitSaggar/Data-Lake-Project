import os
import json
from datetime import datetime

import pandas as pd
from kafka import KafkaConsumer

# ----------------------------
# Kafka Consumer Configuration
# ----------------------------
consumer = KafkaConsumer(
    "clickstream",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="bronze-consumer-group",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

# ----------------------------
# Bronze Folder
# ----------------------------
BRONZE_PATH = "bronze"
os.makedirs(BRONZE_PATH, exist_ok=True)

# ----------------------------
# Batch Settings
# ----------------------------
BATCH_SIZE = 10000
batch = []

print("Listening to Kafka topic: clickstream...")

# ----------------------------
# Consume Messages
# ----------------------------
for message in consumer:

    batch.append(message.value)

    if len(batch) >= BATCH_SIZE:

        df = pd.DataFrame(batch)

        filename = datetime.now().strftime(
            "bronze_%Y%m%d_%H%M%S.parquet"
        )

        filepath = os.path.join(BRONZE_PATH, filename)

        df.to_parquet(
            filepath,
            index=False,
            compression="snappy"
        )

        print(
            f"Saved {len(batch)} records -> {filepath}"
        )

        batch.clear()