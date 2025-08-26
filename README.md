# FastAPI Users API

A simple FastAPI project to manage users with JWT authentication, password hashing, and database integration using SQLAlchemy. Currently structured for PostgreSQL but can be extended to other databases.

## 🗂 Project Structure

fastapi-api/
│
├── main.py          # Entry point of the API, registers routers
├── database.py      # SQLAlchemy database configuration
├── models.py        # ORM models
├── schemas.py       # Pydantic schemas for request/response validation
├── crud.py          # CRUD operations for User model
├── utils.py         # Password hashing and JWT token utilities
├── routers/
│   └── users.py     # User endpoints (register, login, list users)
├── __init__.py      # Python package marker
└── README.md

## 🔧 Features Implemented

- User registration with hashed passwords (bcrypt)
- User login with JWT token generation
- Listing all registered users
- SQLAlchemy ORM integration
- Project structure separated by `routers`, `crud`, `schemas`, `utils`
- `.gitignore` configured to exclude caches, virtual environments, and temp files
- Ready for database connection (PostgreSQL) and future deployment (Railway/Docker)

## ⚡ Planned Features

- Connect the project to PostgreSQL (local or Railway)  
- Add full CRUD operations: update and delete users  
- Add authentication middleware for protected routes  
- Implement Docker containerization  
- Add CI/CD workflow (GitHub Actions)  
- Error handling improvements and validations  

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/RaynerKovachevich/fastapi-users-api.git
cd fastapi-users-api
