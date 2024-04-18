from pydantic import BaseModel, EmailStr, validator
from passlib.context import CryptContext
import uuid




class PostBase(BaseModel):
    title: str
    content: str

class CreatePost(PostBase):
    pass

class Post(PostBase):
    post_id: uuid.UUID
    owner_id: uuid.UUID

    class Config:
        arbitrary_types_allowed = True
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
    user_id: uuid.UUID
    post: list[Post] = []

    class Config:
        arbitrary_types_allowed = True

        orm_mode =True





