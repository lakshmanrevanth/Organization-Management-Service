from database.master import admins
from core.security import verify_password, create_token, hash_password

def login(email: str, password: str):
    admin = admins.find_one({"email": email.lower()})
    if not admin:
        return None

    stored = admin.get("password")
    # Stored password could be bytes (hashed) or string (legacy). Handle both.
    if isinstance(stored, (bytes, bytearray)):
        if not verify_password(password, stored):
            return None
    elif isinstance(stored, str):
        # Legacy storage: plain string. Compare, but then migrate to hashed password.
        if stored != password:
            return None
        # Migrate: update stored password to hashed bytes
        admins.update_one({"_id": admin["_id"]}, {"$set": {"password": hash_password(password)}})
    else:
        # Unknown password format: deny access
        return None

    return create_token({
        "admin_id": str(admin["_id"]),
        "organization": admin["organization"]
    })
