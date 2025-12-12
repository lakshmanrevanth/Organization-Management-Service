from fastapi import FastAPI
from app.routes import organization, auth

app = FastAPI(title="Organization Management Service")

app.include_router(organization.router)
app.include_router(auth.router)
