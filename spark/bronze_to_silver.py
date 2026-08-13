from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    to_timestamp,
    hour,
    dayofmonth,
    month,
    year
)

# -----------------------------------
# Create Spark Session
# -----------------------------------
spark = (
    SparkSession.builder
    .appName("BronzeToSilverETL")
    .getOrCreate()
)

print("Spark Session Created")

# -----------------------------------
# Locate Bronze Folder
# -----------------------------------
project_root = Path(__file__).resolve().parent.parent
bronze_path = project_root / "bronze"
silver_path = project_root / "silver"

print(f"Reading Bronze Layer from: {bronze_path}")

# -----------------------------------
# Read Bronze Layer
# -----------------------------------
bronze_df = spark.read.parquet(str(bronze_path))

print(f"Bronze Records: {bronze_df.count()}")

# -----------------------------------
# Remove Duplicates
# -----------------------------------
bronze_df = bronze_df.dropDuplicates()

# -----------------------------------
# Remove Null Values
# -----------------------------------
bronze_df = bronze_df.dropna()

# -----------------------------------
# Convert Timestamp
# -----------------------------------
bronze_df = bronze_df.withColumn(
    "timestamp",
    to_timestamp("timestamp")
)

# -----------------------------------
# Convert Numeric Columns
# -----------------------------------
bronze_df = (
    bronze_df
    .withColumn("price", col("price").cast("double"))
    .withColumn("quantity", col("quantity").cast("integer"))
    .withColumn("session_duration", col("session_duration").cast("integer"))
)

# -----------------------------------
# Apply Business Rules
# -----------------------------------
bronze_df = bronze_df.filter(col("price") > 0)

# -----------------------------------
# Create Derived Columns
# -----------------------------------
bronze_df = (
    bronze_df
    .withColumn("hour", hour("timestamp"))
    .withColumn("day", dayofmonth("timestamp"))
    .withColumn("month", month("timestamp"))
    .withColumn("year", year("timestamp"))
)

print(f"Silver Records: {bronze_df.count()}")

# -----------------------------------
# Write Silver Layer
# -----------------------------------
(
    bronze_df
    .write
    .mode("overwrite")
    .partitionBy("year", "month")
    .parquet(str(silver_path))
)

print("Silver Layer Created Successfully!")

spark.stop()