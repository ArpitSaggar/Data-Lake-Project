import os
import sys
import pandas as pd
from pathlib import Path
import shutil

print("Changing to data_generator directory...")
os.chdir(r"c:\Users\LENOVO\DataLakeProject\data_generator")
print("Running clickstream_generator.py...")
with open("clickstream_generator.py", "r") as f:
    exec(f.read())

print("Reading clickstream_data.csv...")
df = pd.read_csv("clickstream_data.csv")

bronze_path = r"c:\Users\LENOVO\DataLakeProject\bronze"
if os.path.exists(bronze_path):
    shutil.rmtree(bronze_path)
os.makedirs(bronze_path)

print("Writing to bronze layer...")
df.to_parquet(os.path.join(bronze_path, "data.parquet"), index=False)

print("Changing to spark directory...")
os.chdir(r"c:\Users\LENOVO\DataLakeProject\spark")

print("Running bronze_to_silver.py...")
os.system(r"..\venv\Scripts\python bronze_to_silver.py")

print("Running silver_to_gold.py...")
os.system(r"..\venv\Scripts\python silver_to_gold.py")

print("Data regenerated successfully!")
