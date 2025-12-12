from app.db.master import admins
from app.core.security import verify_password, create_token

def login(email: str, password: str):
    admin = admins.find_one({"email": email})
    if not admin or not verify_password(password, admin["password"]):
        return None

    return create_token({
        "admin_id": str(admin["_id"]),
        "organization": admin["organization"]
    })
