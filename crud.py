from sqlalchemy.orm import Session
import models, schemas

# Create a new user

def create_user(db: Session, user: schemas.UserCreate):
    """
    Insert a new user into the database.
    """

    db_user = models.User(
        email=user .email,
        hashed_password=user.password,
        is_active=user.is_activate
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get all users
def get_users(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrive a list of users from the database.
    Paginacion supported with skip en limit.
    """
    return db.query(models.user).offset(skip).limit(limit).all()

# Get one user by ID
def get_user(db: Session, user_id: int):
    """
    Retrive a single user by teheir ID.
    """
    return db.query(models.user).filter(models.user.id == user_id).first()

# Get user by email
def get_user_by_email(db: Session, email: str):
    """
    Retrive a single user by their email.
    """
    return db.query(models.user).filter(models.user.email == email).first()