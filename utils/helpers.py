import re

def sanitize_org_name(name: str) -> str:
    name = name.lower().strip()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_")

def tenant_collection_name(org_name: str) -> str:
    return f"org_{sanitize_org_name(org_name)}"
