# FastAPI Users API

[![CI](https://github.com/RaynerKovachevich/fastapi-users-api/actions/workflows/python-app.yml/badge.svg)](https://github.com/RaynerKovachevich/fastapi-users-api/actions/workflows/python-app.yml)

A simple FastAPI project to manage users with JWT authentication, password hashing, and database integration using SQLAlchemy. Currently structured for PostgreSQL with Docker support and GitHub Actions CI.

## 🗂 Project Structure

fastapi-api/
├── main.py # Entry point of the API, registers routers
├── database.py # SQLAlchemy database configuration
├── models.py # ORM models
├── schemas.py # Pydantic schemas for request/response validation
├── crud.py # CRUD operations for User model
├── utils.py # Password hashing and JWT token utilities
├── routers/
│   └── users.py # User endpoints (register, login, list users)
├── init.py # Python package marker
├── Dockerfile # Docker configuration for API
├── docker-compose.yml # Docker Compose for API + PostgreSQL
├── requirements.txt # Python dependencies
└── README.md

## 🔧 Features Implemented

- User registration with hashed passwords (bcrypt)
- User login with JWT token generation
- Listing all registered users
- SQLAlchemy ORM integration
- Project structured with routers, CRUD, schemas, utils
- Dockerized for easy local development and deployment
- GitHub Actions CI pipeline for automatic testing on push
- Tests passing successfully ✅

## ⚡ Planned Features

- Full CRUD operations: update and delete users
- Authentication middleware for protected routes
- Error handling improvements and validations
- Optional deployment CD pipeline

## 🚀 Getting Started

1. Clone the repository:

bash
git clone https://github.com/RaynerKovachevich/fastapi-users-api.git
cd fastapi-users-api
Build and start the Docker containers:

bash
Copy code
docker compose up --build
The API will be available at http://localhost:8000.

Run tests locally (optional):

bash
Copy code
pytest -v
🏗 CI/CD
This project uses GitHub Actions for continuous integration. Every push triggers:

Dependency installation

Running tests via pytest

Reporting success/failure directly in GitHub

