from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud import create_user, create_message, get_user, get_users, get_messages, get_user_by_username
from schemas import UserCreate, User, MessageCreate, Message
from database import SessionLocal

# Create a new router instance
router = APIRouter()

def get_db():
    """
    Dependency that provides a SQLAlchemy session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db=db, user=user)

@router.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of users.
    """
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.post("/messages/", response_model=Message)
def create_new_message(message: MessageCreate, db: Session = Depends(get_db)):
    """
    Create a new message.
    """
    return create_message(db=db, message=message)

@router.get("/messages/", response_model=List[Message])
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of messages.
    """
    messages = get_messages(db, skip=skip, limit=limit)
    return messages
