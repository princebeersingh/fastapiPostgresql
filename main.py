from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app =FastAPI()


class Post(BaseModel):
      title:str
      content:str
      published: bool = True
      rating: Optional[int] = None
 
@app.get("/")
async def root():
      return {"message": "to app"}

@app.get("/posts")
def get_posts():
      return {"data": "this is your post"}

@app.post("/createposts")
def create_posts(post:Post):#here data converted into python dictionary
      print(post)
      print(post.dict())
      return {"data":post}
# title -string, content -string , category, bool published