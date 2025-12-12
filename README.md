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

- - POST	/org/create	Create organization
<img width="1171" height="1024" alt="image" src="https://github.com/user-attachments/assets/17dc70f8-4ff4-4c93-af5d-703a066e9b2d" />
- - GET	/org/get	Get organization
<img width="1169" height="975" alt="image" src="https://github.com/user-attachments/assets/b27ee2cf-51f1-4b99-8873-67e1c5ab60b9" />
- - POST	/admin/login	Admin login
<img width="1183" height="949" alt="image" src="https://github.com/user-attachments/assets/5dfbbf4c-c6c1-430b-933f-ebd93c888eb1" />
- - PUT	/org/update	Update organization
<img width="1114" height="927" alt="image" src="https://github.com/user-attachments/assets/0ffe0088-1143-43d8-a153-08c11f055325" />
- - DELETE	/org/delete	Delete organization
<img width="1103" height="885" alt="image" src="https://github.com/user-attachments/assets/cd7264fe-3ebd-48d9-902d-d8bb30f43e87" />

 




