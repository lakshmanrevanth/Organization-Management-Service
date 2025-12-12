from database.mongo import get_master_db

db = get_master_db()

organizations = db["organizations"]
admins = db["admins"]
