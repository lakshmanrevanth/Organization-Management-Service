from fastapi import FastAPI
from routes import organization, auth

app = FastAPI(title="Organization Management Service")

app.include_router(organization.router)
app.include_router(auth.router)
