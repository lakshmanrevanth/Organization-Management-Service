from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:27yQRuXUUP0lmLQ2@org-cluster.g4bojiu.mongodb.net/?appName=org-cluster")
db = client["test_db"]

db.test.insert_one({"msg": "MongoDB Connected"})
print("Connected Successfully")
