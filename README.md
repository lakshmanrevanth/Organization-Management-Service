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
- git clone https://github.com/yourname/org-management-service
- cd org-management-service
- pip install -r requirements.txt
- python -m uvicorn main:app --reload

4. Environment Variables
- MONGODB_URI=
- MASTER_DB=organization_master
- SECRET_KEY=supersecretkey
- TOKEN_EXPIRE_MINUTES=60

5.              ┌────────────────────┐
                │      Client        │
                │ (Postman / Browser)│
                └─────────┬──────────┘
                          │ HTTP Requests
                          ▼
                ┌────────────────────┐
                │     FastAPI App     │
                │   (main.py)         │
                └─────────┬──────────┘
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
        ▼                                   ▼
┌────────────────────┐             ┌────────────────────┐
│  Organization APIs │             │    Admin APIs       │
│  /org/create       │             │  /admin/login       │
│  /org/get          │             └─────────┬──────────┘
│  /org/update       │                       │
│  /org/delete       │                       │ JWT
└─────────┬──────────┘                       ▼
          │                           ┌────────────────────┐
          │                           │ Authentication Layer│
          │                           │ (JWT + bcrypt)      │
          │                           └─────────┬──────────┘
          │                                     │
          ▼                                     ▼
┌────────────────────────────────────────────────────────┐
│                    Service Layer                        │
│  organization_service.py | auth_service.py              │
│  - Business logic                                      │
│  - Authorization checks                                │
│  - Tenant isolation                                    │
└─────────┬───────────────────────────┬──────────────────┘
          │                           │
          ▼                           ▼
┌────────────────────┐       ┌──────────────────────────┐
│   Master Database  │       │   Tenant Collections     │
│ (MongoDB)          │       │ (MongoDB)                │
│                    │       │                          │
│ - organizations    │       │ - org_revant             │
│ - admins           │       │ - org_acme_corp          │
│                    │       │ - org_companyX           │
└────────────────────┘       └──────────────────────────┘

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

 -- Brief notes explaining the design choices --

1️⃣ Multi-Tenant Architecture

A master database stores organization and admin details, while each organization gets its own MongoDB collection for data isolation.

2️⃣ Separation of Concerns

The project is divided into routes, services, security, and database layers to keep the code clean, modular, and easy to maintain.

3️⃣ Authentication & Authorization

Admins log in using JWT tokens, and all protected actions are authorized by validating the admin and organization from the database.

4️⃣ Dynamic Collection Strategy

When an organization is created or renamed, MongoDB collections are created or migrated dynamically to support multi-tenancy.

5️⃣ Security Choices

Passwords are securely hashed using bcrypt, JWT tokens have expiration, and secrets are stored using environment variables.

6️⃣ Deployment Friendly

The application is cloud-ready, binds to dynamic ports, and can easily switch between local MongoDB and MongoDB Atlas.





