from sqlalchemy.orm import Session
from models import User, Message
from schemas import UserCreate, MessageCreate

def get_user(db: Session, user_id: int):
    """
    Get a user by its ID.
    """
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    """
    Get a user by its username.
    """
    return db.query(User).filter(User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    """
    Get a list of users with optional pagination.
    """
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    """
    Create a new user.
    """
    db_user = User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_message(db: Session, message: MessageCreate):
    """
    Create a new message.
    """
    db_message = Message(content=message.content, user_id=message.user_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages(db: Session, skip: int = 0, limit: int = 10):
    """
    Get a list of messages with optional pagination.
    """
    return db.query(Message).offset(skip).limit(limit).all()
