from sqlalchemy.orm import Session
from . import models, schemas



#Get User By ID

def getUserByID(db: Session, id: str):
    return db.query(models.User).filter(models.User.user_id == id).first()


# Get user by email
def getUserByEmail(db: Session, email: str):
    return db.query(models.User).filter(models.User.email ==email).first()


#Get all users

def getAllUsers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Creating a new user
def createUser(db: Session, user: schemas.CreateUser):
    db_user =models.User(email=user.email, username=user.username, fullname=user.fullname, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User successflly created", "user details" : db_user}



# Get all post

def getAllPost(db: Session, skip: int =0, limit: int =100):
    return db.query(models.Post).offset(skip).limit(limit).all()

# Get post by id

def getPostByID(db: Session, id: str):
    return db.query(models.Post).filter(models.Post.post_id ==id).first()

# Get post by date

def getPostBydate(db: Session, p_date):
    return db.query(models.Blog).filter(models.Blog.created_date==p_date).first()

# creating a post
def createPost(db: Session, post: schemas.CreatePost, user_id: str):
    db_post = models.Post(**post.model_dump(), owner_id = user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
