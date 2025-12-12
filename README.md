# Organization-Management-Service

1. Project Overview
Multi-tenant Organization Management Service built using FastAPI and MongoDB.
Each organization has an isolated MongoDB collection with JWT-based admin authentication.

2. Tech Stack
- FastAPI
- MongoDB
- JWT Authentication
- bcrypt

3. Setup Instructions
git clone https://github.com/yourname/org-management-service
cd org-management-service
pip install -r requirements.txt
uvicorn app.main:app --reload

4. Environment Variables
- MONGODB_URI=mongodb+srv://admin:27yQRuXUUP0lmLQ2@org-cluster.g4bojiu.mongodb.net/?appName=org-cluster
- MASTER_DB=organization_master
- SECRET_KEY=supersecretkey
- TOKEN_EXPIRE_MINUTES=60

6. API Endpoints Table
- Method	Endpoint	Description
- POST	/org/create	Create organization
- GET	/org/get	Get organization
- PUT	/org/update	Update organization
- DELETE	/org/delete	Delete organization
- POST	/admin/login	Admin login

<img width="1355" height="1001" alt="image" src="https://github.com/user-attachments/assets/b35603b6-2d38-436e-b5f9-5bdf05088ee5" />
 


