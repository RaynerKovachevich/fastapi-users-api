from sqlalchemy.orm import Session
import models, schemas

# -------------------------
# Create a new user
# -------------------------
def create_user(db: Session, user: schemas.UserCreate):
    """
    Insert a new user into the database.
    """
    db_user = models.User(
        username=user.username,  
        email=user.email,
        password=user.password,
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# -------------------------
# Get all users
# -------------------------
def get_users(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of users from the database.
    Pagination supported with skip and limit.
    """
    return db.query(models.User).offset(skip).limit(limit).all()

# -------------------------
# Get one user by ID
# -------------------------
def get_user(db: Session, user_id: int):
    """
    Retrieve a single user by their ID.
    """
    return db.query(models.User).filter(models.User.id == user_id).first()

# -------------------------
# Get user by email
# -------------------------
def get_user_by_email(db: Session, email: str):
    """
    Retrieve a single user by their email.
    """
    return db.query(models.User).filter(models.User.email == email).first()
