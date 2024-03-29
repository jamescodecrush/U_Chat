from sqlalchemy.orm import Session
from . import models, schemas

# Creating a new user
def creat_user(db: Session, user: schemas.CreateUser) :

    db_user =models.User(email =user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Get User By ID

def getUser_by_ID(db: Session, id: str):
    return db.query(models.User).filter(models.User.user_id==id).first()


# Get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email ==email).first()


#Get all users

def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Let create a post

def create_post(db: Session, post: schemas.CreatePost, user_id: str):
    db_post = models.CreatePost(**post.model_dump(), owner_id = user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Get post by id

def get_post_by_id(db: Session, id: str):
    return db.query(models.Post).filter(models.Post.post_id ==id).first()

# Get post by date

def get_post_by_date(db: Session, p_date):
    return db.query(models.Blog).filter(models.Blog.created_date==p_date).first()

# Get all post

def get_all_post(db: Session, skip: int =0, limit: int =100):
    return db.query(models.Post).offset(skip).limit(limit).all()