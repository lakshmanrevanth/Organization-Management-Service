from pymongo import MongoClient
from app.core.config import settings

client = MongoClient(settings.MONGODB_URI)

def get_master_db():
    return client[settings.MASTER_DB]
