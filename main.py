from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

# Secret key for JWT token (in production, use environment variable)
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Create FastAPI instance
app = FastAPI(title="FastAPI Users API", version="1.0")

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# In-memory "database"
users_db = []

# Pydantic models
class User(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    username: str
    email: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Utility functions
def hash_password(password: str):
    """Hash a plain password"""
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """Verify a password against its hash"""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    """Create JWT token"""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Endpoints
@app.get("/")
def read_root():
    """Root endpoint to check API status"""
    return {"message": "User API is working"}

@app.post("/users/register", response_model=UserOut)
def register_user(user: User):
    """Register a new user"""
    for u in users_db:
        if u["username"] == user.username:
            raise HTTPException(status_code=400, detail="Username already exists")
    hashed_pw = hash_password(user.password)
    users_db.append({"username": user.username, "email": user.email, "password": hashed_pw})
    return {"username": user.username, "email": user.email}

@app.post("/users/login", response_model=Token)
def login_user(user: UserLogin):
    """Login user and return JWT token"""
    db_user = next((u for u in users_db if u["username"] == user.username), None)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": token, "token_type": "bearer"}

@app.get("/users", response_model=List[UserOut])
def get_users():
    """Get list of registered users"""
    return [{"username": u["username"], "email": u["email"]} for u in users_db]
