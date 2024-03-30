from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# The Dependency

def get_db():
    db = SessionLocal()
    try: yield db

    finally: 
        db.close()
    

# Endpoint for creating users    

@app.post("users/", response_model= schemas.User)
def create_user(user: schemas.CreateUser, db: Session =Depends(get_db)):
        db_user = crud.get_user_by_email(db, email=user.email)
        if db_user:
            raise HTTPException(status_code= 400, detail="This email is already registered with another account. Please try again with new email")
        return crud.creat_user(db=db, user=user)

# Endpoint to get uses by id

@app.get("/users/, {user_id}", response_model=schemas.User)
def read_user(user_id: str, db: Session=Depends(get_db)):
     db_user = crud.get_post_by_id(db, user_id=user_id)
     if db_user is None:
          raise HTTPException(status_code=404, detail="User not found")
     return db_user


#Endpoint to get all users

@app.get("/users/", response_model= list[schemas.User])
def read_users(skip: 0, limit = 10, db:Session = Depends(get_db)):
     users = crud.get_all_users(db, skip=skip, limit=limit)

     return users

# NOW WE ABOUT TO CREAT THE POST

#Endpoint to creat post

@app.post("/users/{user_id}/posts/", response_model=schemas.Post)
def creat_post_by_user(user_id: str, post: schemas.CreatePost, db: Session = Depends(get_db)):
            return crud.create_post(db=db, post=post, user_id=user_id)           


#Endpoint to get post

@app.get("/posts/", response_model=list[schemas.Post])
def read_post(skip: int =0, limit: int = 10, db: Session =Depends(get_db)):
      posts = crud.get_all_post(db, skip=skip, limit=limit)
      return posts