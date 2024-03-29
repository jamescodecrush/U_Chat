from pydantic import BaseModel, EmailStr, validator
from sqlalchemy import UUID
from passlib.context import CryptContext




class PostBase(BaseModel):
    title: str
    content: str

class CreatePost(PostBase):
    pass

class Post(PostBase):
    post_id: UUID
    owner_id: str

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    fullname: str
    email: EmailStr 
    username: str

class CreateUser(UserBase):
    password: str

    @validator('password', pre=True)
    def hash_password(cls, value):

     hashed_password = CryptContext(schemes=["bcrypt"], deprecated="auto").hash(value)
     return hashed_password




class User(UserBase):
    user_id: UUID
    post: list[Post] = []

    class Config:

        orm_mode =True





