from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql.functions import count, sum, avg

# -----------------------------
# Project Paths
# -----------------------------
project_root = Path(__file__).resolve().parent.parent
silver_path = project_root / "silver"
gold_path = project_root / "gold"

# -----------------------------
# Spark Session
# -----------------------------
spark = (
    SparkSession.builder
    .appName("SilverToGold")
    .getOrCreate()
)

print("Spark Session Created")

# -----------------------------
# Read Silver Layer
# -----------------------------
print(f"Reading Silver Layer from: {silver_path}")

df = spark.read.parquet(str(silver_path))

print("Silver Records:", df.count())

# -----------------------------
# 1. Page Analytics
# -----------------------------
page_stats = (
    df.groupBy("page")
      .agg(
          count("*").alias("total_visits"),
          sum("price").alias("total_revenue"),
          avg("price").alias("avg_price")
      )
)

page_stats.write.mode("overwrite").parquet(
    str(gold_path / "page_analytics")
)

print("Page Analytics Created")

# -----------------------------
# 2. Device Analytics
# -----------------------------
device_stats = (
    df.groupBy("device")
      .agg(
          count("*").alias("visits"),
          sum("price").alias("revenue"),
          avg("price").alias("avg_price")
      )
)

device_stats.write.mode("overwrite").parquet(
    str(gold_path / "device_analytics")
)

print("Device Analytics Created")

# -----------------------------
# 3. Referral Source Analytics
# -----------------------------
traffic_stats = (
    df.groupBy("referral_source")
      .agg(
          count("*").alias("visits"),
          sum("price").alias("revenue"),
          avg("price").alias("avg_price")
      )
)

traffic_stats.write.mode("overwrite").parquet(
    str(gold_path / "traffic_analytics")
)

print("Referral Source Analytics Created")

# -----------------------------
# 4. Category Analytics
# -----------------------------
category_stats = (
    df.groupBy("category")
      .agg(
          count("*").alias("orders"),
          sum("quantity").alias("items_sold"),
          sum("price").alias("revenue"),
          avg("price").alias("avg_price")
      )
)

category_stats.write.mode("overwrite").parquet(
    str(gold_path / "category_analytics")
)

print("Category Analytics Created")

# -----------------------------
# 5. Purchase Analytics
# -----------------------------
purchase_stats = (
    df.groupBy("is_purchase")
      .agg(
          count("*").alias("events"),
          sum("price").alias("revenue")
      )
)

purchase_stats.write.mode("overwrite").parquet(
    str(gold_path / "purchase_analytics")
)

print("Purchase Analytics Created")

# -----------------------------
# 6. Browser Analytics
# -----------------------------
browser_stats = (
    df.groupBy("browser")
      .agg(
          count("*").alias("visits"),
          sum("price").alias("revenue")
      )
)

browser_stats.write.mode("overwrite").parquet(
    str(gold_path / "browser_analytics")
)

print(" Browser Analytics Created")

# -----------------------------
# 7. Operating System Analytics
# -----------------------------
os_stats = (
    df.groupBy("operating_system")
      .agg(
          count("*").alias("visits"),
          sum("price").alias("revenue")
      )
)

os_stats.write.mode("overwrite").parquet(
    str(gold_path / "os_analytics")
)

print(" Operating System Analytics Created")

print("\n=====================================")
print(" GOLD LAYER CREATED SUCCESSFULLY!")
print("=====================================")

spark.stop()