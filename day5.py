import pandas as pd
import numpy as np
from pymongo import MongoClient

# Step 1: Load CSV from Day 4
df = pd.read_csv("countries_gdp.csv")

# Step 2: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Default port
db = client["world_data"]  # Database name
collection = db["gdp"]  # Collection name

# Step 3: Convert DataFrame to dictionary and insert
data = df.to_dict("records")
collection.insert_many(data)


print(f"Inserted {len(data)} documents into MongoDB!")