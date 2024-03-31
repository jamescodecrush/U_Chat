from sqlalchemy import Column, Integer, UUID, String, Text, ForeignKey, DateTime
# from  sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
import uuid

# Base = declarative_base()

class User(Base):
    __tablename__ ="users"
    user_id = Column(UUID(as_uuid= True), primary_key=True, default= uuid.uuid4, index=True)
    fullname = Column(String(200), nullable= False)
    username =Column(String(60), unique= True, nullable=False)
    email = Column(String(120), unique= True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    
    post = relationship("Blog", back_populates= "owner_id")
    
class Blog(Base):
    __tablename__ ="blog"
    post_id = Column(UUID(as_uuid=True), primary_key= True, unique=True, index=True)
    title = Column(String(255), nullable=False )
    content = Column(Text, nullable= False)
    created_date = Column(DateTime(timezone=True), server_default= func.now())
    created_date = Column(DateTime(timezone=True), onupdate= func.now())
    owner_id = (String, ForeignKey("users.user_id"))

    owner_id = relationship("Users", back_populates= "post")


