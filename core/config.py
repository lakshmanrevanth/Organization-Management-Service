import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    MASTER_DB = os.getenv("MASTER_DB_NAME", "organization_master")

    SECRET_KEY = os.getenv("SECRET_KEY", "change_me")
    ALGORITHM = "HS256"
    TOKEN_EXPIRE_MINUTES = 60

settings = Settings()
