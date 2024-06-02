from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    """
    Represents a user in the chat application.

    Attributes:
        id: Unique identifier for the user.
        username: Username of the user.
        messages: Relationship to the Message model.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    messages = relationship("Message", back_populates="user")

class Message(Base):
    """
    Represents a message in the chat application.

    Attributes:
        id: Unique identifier for the message.
        content: Content of the message.
        user_id: Foreign key to the User model.
        user: Relationship to the User model.
    """
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="messages")
