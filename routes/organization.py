from fastapi import APIRouter, Depends, HTTPException
from models import organization
from models.organization import OrgCreate, OrgUpdate, OrgDelete
from services.organization_service import (
    create_organization,
    get_organization_by_name,
    update_organization,
    delete_organization,
)
from core.security import get_current_admin
from database.master import organizations

router = APIRouter(
    prefix="/org",
    tags=["Organization"]
)

@router.post("/create")
def create_org(data: OrgCreate):
    try:
        org = create_organization(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Organization created", "organization": org}

@router.put("/update")
def update_org(data: OrgUpdate, admin=Depends(get_current_admin)):
    try:
        updated = update_organization(data, admin)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    return {"message": "Organization updated", "organization": updated}

@router.delete("/delete")
def delete_org(data: OrgDelete, admin=Depends(get_current_admin)):
    try:
        delete_organization(data.organization_name, admin)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    return {"message": "Organization deleted"}


@router.get("/get")
def get_org(organization_name: str):
    org = get_organization_by_name(organization_name)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org

@router.get("/all")
def get_all_organizations():
    orgs = list(organizations.find({}, {"_id": 0}))
    return {
        "count": len(orgs),
        "organizations": orgs
    }

