from fastapi import APIRouter, HTTPException, Depends
from app.models.organization import OrgCreate
from app.services.organization_service import create_organization
from app.core.security import get_current_admin

router = APIRouter(prefix="/org")

@router.post("/create")
def create_org(data: OrgCreate):
    try:
        create_organization(data)
        return {"message": "Organization created"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
