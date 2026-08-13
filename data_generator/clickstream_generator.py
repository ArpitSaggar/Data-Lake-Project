import random
import uuid
from datetime import datetime, timedelta
from faker import Faker

# Create Faker object
fake = Faker()

# ==========================================
# CONFIGURATION
# ==========================================

# Number of events to generate
NUM_EVENTS = 1000000

# Number of unique users
NUM_USERS = 1000

# Event Types
EVENT_TYPES = [
    "View Product",
    "Search",
    "Add to Cart",
    "Remove from Cart",
    "Purchase"
]

# Website Pages
PAGES = [
    "Home",
    "Search",
    "Product",
    "Cart",
    "Checkout"
]

# Devices
DEVICES = [
    "Mobile",
    "Laptop",
    "Tablet"
]

# Browsers
BROWSERS = [
    "Chrome",
    "Edge",
    "Firefox",
    "Safari"
]

# Operating Systems
OPERATING_SYSTEMS = [
    "Windows",
    "Android",
    "iOS",
    "macOS"
]

# Referral Sources
REFERRAL_SOURCES = [
    "Google",
    "Facebook",
    "Instagram",
    "Email",
    "Direct"
]

QUANTITIES = [1, 2, 3, 4, 5]

CAMPAIGNS = [
    "Summer Sale",
    "Flash Sale",
    "Black Friday",
    "Diwali Offer",
    "New User",
    "No Campaign"
]

# ==========================================
# PRODUCT CATALOG
# ==========================================

PRODUCTS = [
    {
        "product_id": "P001",
        "product_name": "iPhone 17",
        "category": "Electronics",
        "price": 999
    },
    {
        "product_id": "P002",
        "product_name": "Samsung Galaxy S26",
        "category": "Electronics",
        "price": 899
    },
    {
        "product_id": "P003",
        "product_name": "Sony WH-1000XM6",
        "category": "Electronics",
        "price": 399
    },
    {
        "product_id": "P004",
        "product_name": "Nike Air Max",
        "category": "Fashion",
        "price": 150
    },
    {
        "product_id": "P005",
        "product_name": "Levi's Jeans",
        "category": "Fashion",
        "price": 80
    },
    {
        "product_id": "P006",
        "product_name": "Apple MacBook Pro",
        "category": "Electronics",
        "price": 2499
    },
    {
        "product_id": "P007",
        "product_name": "Dell XPS 15",
        "category": "Electronics",
        "price": 1999
    },
    {
        "product_id": "P008",
        "product_name": "Instant Coffee",
        "category": "Grocery",
        "price": 12
    },
    {
        "product_id": "P009",
        "product_name": "Office Chair",
        "category": "Furniture",
        "price": 220
    },
    {
        "product_id": "P010",
        "product_name": "Mechanical Keyboard",
        "category": "Electronics",
        "price": 120
    }
]

# ==========================================
# USER CATALOG
# ==========================================

USERS = []

for i in range(NUM_USERS):
    USERS.append({
        "user_id": f"U{i+1:06}",
        "city": fake.city(),
        "country": fake.country()
    })

# ==========================================
# GENERATE CLICKSTREAM EVENTS
# ==========================================

events = []

for _ in range(NUM_EVENTS):

    user = random.choice(USERS)
    product = random.choice(PRODUCTS)
    event_type = random.choice(EVENT_TYPES)
    is_purchase = event_type == "Purchase"
    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": fake.date_time_between(
            start_date="-30d",
            end_date="now"
        ),
        "user_id": user["user_id"],
        "city": user["city"],
        "country": user["country"],
        "session_id": str(uuid.uuid4()),
        "event_type": event_type,
        "page": random.choice(PAGES),
        "product_id": product["product_id"],
        "product_name": product["product_name"],
        "category": product["category"],
        "price": product["price"],
        "device": random.choices(DEVICES, weights=[60, 30, 10], k=1)[0],
        "browser": random.choices(BROWSERS, weights=[50, 25, 15, 10], k=1)[0],
        "operating_system": random.choices(OPERATING_SYSTEMS, weights=[40, 35, 20, 5], k=1)[0],
        "referral_source": random.choices(REFERRAL_SOURCES, weights=[45, 25, 15, 10, 5], k=1)[0],
        "quantity": random.choice(QUANTITIES),
        "campaign": random.choice(CAMPAIGNS),
        "session_duration": random.randint(10, 1800),
        "is_purchase": is_purchase,
    }

    events.append(event)

# ==========================================
# SAVE TO CSV
# ==========================================

import pandas as pd

df = pd.DataFrame(events)

df.to_csv("clickstream_data.csv", index=False)

print(f"Successfully generated {len(df)} clickstream events.")
print("File saved as clickstream_data.csv")


