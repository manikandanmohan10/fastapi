import os
from pymongo.mongo_client import MongoClient

client = MongoClient(os.getenv('MONGO_URL'))

db = client.sample_airbnb

collection_name = db["users"]