from fastapi import APIRouter, HTTPException
from models.auth import LoginRequest
from services.auth_service import login

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.post("/login")
def admin_login(data: LoginRequest):
    token = login(data.email, data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token}
