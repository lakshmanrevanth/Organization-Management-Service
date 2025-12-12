from app.db.master import organizations, admins
from app.db.mongo import client
from app.utils.helpers import tenant_collection_name
from app.core.security import hash_password
from datetime import datetime

def create_organization(data):
    if organizations.find_one({"organization_name": data.organization_name}):
        raise ValueError("Organization already exists")

    collection = tenant_collection_name(data.organization_name)
    db = client.get_database()
    db.create_collection(collection)

    admin = {
        "email": data.email,
        "password": hash_password(data.password),
        "organization": data.organization_name
    }
    admin_id = admins.insert_one(admin).inserted_id

    organizations.insert_one({
        "organization_name": data.organization_name,
        "collection": collection,
        "admin_id": str(admin_id),
        "created_at": datetime.utcnow()
    })
