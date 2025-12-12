from pydantic import BaseModel, EmailStr

class OrgCreate(BaseModel):
    organization_name: str
    email: EmailStr
    password: str

class OrgUpdate(BaseModel):
    old_organization_name: str
    new_organization_name: str
    email: EmailStr | None = None
    password: str | None = None


class OrgDelete(BaseModel):
    organization_name: str
