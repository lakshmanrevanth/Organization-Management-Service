import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGODB_URI = os.getenv("MONGODB_URI")
    MASTER_DB = os.getenv("MASTER_DB", "organization_master")

    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    TOKEN_EXPIRE_MINUTES = int(os.getenv("TOKEN_EXPIRE_MINUTES", 60))


settings = Settings()
