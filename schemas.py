from pydantic import BaseModel

class MessageBase(BaseModel):
    """
    Base schema for a message.
    """
    content: str
    user_id: int

class MessageCreate(MessageBase):
    """
    Schema for creating a new message.
    """
    pass

class Message(MessageBase):
    """
    Schema for reading a message.
    """
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    """
    Base schema for a user.
    """
    username: str

class UserCreate(UserBase):
    """
    Schema for creating a new user.
    """
    pass

class User(UserBase):
    """
    Schema for reading a user.
    """
    id: int
    messages: list[Message] = []

    class Config:
        orm_mode = True
