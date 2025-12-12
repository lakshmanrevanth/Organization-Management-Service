from database.master import organizations, admins
from database.mongo import client
from core.config import settings
from utils.helpers import tenant_collection_name
from core.security import hash_password
from datetime import datetime
from bson import ObjectId

def create_organization(data):
    if organizations.find_one({"organization_name": data.organization_name}):
        raise ValueError("Organization already exists")

    db = client[settings.MASTER_DB]   # ✅ FIX HERE

    collection_name = tenant_collection_name(data.organization_name)

    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)

    admin = {
        "email": data.email,
        "password": hash_password(data.password),
        "organization": data.organization_name,
        "created_at": datetime.utcnow()
    }

    admin_id = admins.insert_one(admin).inserted_id

    organizations.insert_one({
        "organization_name": data.organization_name,
        "collection": collection_name,
        "admin_id": str(admin_id),
        "created_at": datetime.utcnow()
    })

    return {
        "organization_name": data.organization_name,
        "collection": collection_name,
        "admin_id": str(admin_id)
    }


def get_organization_by_name(org_name: str):
    return organizations.find_one({"organization_name": org_name}, {"_id": 0})


def update_organization(data, admin):
    existing = organizations.find_one({"organization_name": data.organization_name})
    if not existing:
        raise ValueError("Organization does not exist")

    # Only allow admin of the org to update
    if admin and admin.get("organization") != data.organization_name:
        raise PermissionError("Not authorized to update this organization")

    db = client[settings.MASTER_DB]
    old_collection = existing["collection"]

    new_name = data.new_organization_name or data.organization_name
    if new_name != data.organization_name:
        if organizations.find_one({"organization_name": new_name}):
            raise ValueError("New organization name already exists")

        new_collection = tenant_collection_name(new_name)
        if new_collection not in db.list_collection_names():
            db.create_collection(new_collection)

        # copy documents from old to new collection (without preserving _id to avoid conflicts)
        docs = list(db[old_collection].find())
        for d in docs:
            d.pop("_id", None)
        if docs:
            db[new_collection].insert_many(docs)

        # drop old collection
        if old_collection != new_collection and old_collection in db.list_collection_names():
            db.drop_collection(old_collection)

        # update organization metadata
        organizations.find_one_and_update(
            {"organization_name": data.organization_name},
            {"$set": {"organization_name": new_name, "collection": new_collection}}
        )

        # update admin's organization field if needed
        admins.update_many({"organization": data.organization_name}, {"$set": {"organization": new_name}})

    # update admin email/password if provided
    if data.email or data.password:
        update_fields = {}
        if data.email:
            update_fields["email"] = data.email
        if data.password:
            update_fields["password"] = hash_password(data.password)
        if update_fields:
            admins.update_one({"_id": ObjectId(existing["admin_id"])}, {"$set": update_fields})

    return get_organization_by_name(new_name)


def delete_organization(org_name: str, admin):
    existing = organizations.find_one({"organization_name": org_name})
    if not existing:
        raise ValueError("Organization does not exist")

    if admin and admin.get("organization") != org_name:
        raise PermissionError("Not authorized to delete this organization")

    db = client[settings.MASTER_DB]
    collection_name = existing["collection"]
    if collection_name in db.list_collection_names():
        db.drop_collection(collection_name)

    # delete admin by id
    try:
        admins.delete_one({"_id": ObjectId(existing["admin_id"])})
    except Exception:
        pass

    organizations.delete_one({"organization_name": org_name})

    return True
