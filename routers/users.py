from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

import models, schemas, crud
from database import get_db
from utils import hash_password, verify_password, create_access_token

# Create router for user endpoints
router = APIRouter(
    prefix="/users", 
    tags=["users"] 
)


@router.post("/", response_model=schemas.UsersOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user in the database.
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user.password = hash_password(user.password)
    return crud.create_user(db=db, user=user)

@router.post("/login", response_model=schemas.Token)
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    Aurhrnticate user and retunr JWT token.
    """
    db_user = crud.get_user_by_email(db, email=user.username)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password ")
    
    token = create_access_token(
       data={"sub": db_user.email},
       expires_delta=timedelta(minutes=30)
   )
    return {"acces_token": token, "token_type": "bearer"}

@router.get("/", response_model=list[schemas.UserOut])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Return list of users from the database.
    """ 
    return crud.get_users(db=db, skip=skip, limit=limit)
    