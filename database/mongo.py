from pymongo import MongoClient
from core.config import settings

client = MongoClient(
    settings.MONGODB_URI,
    serverSelectionTimeoutMS=5000
)

def get_master_db():
    return client[settings.MASTER_DB]
