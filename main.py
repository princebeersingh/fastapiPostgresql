from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


app =FastAPI()


class Post(BaseModel):
      title:str
      content:str
      published: bool = True
      rating: Optional[int] = None

my_posts =[{"title":"title 1", "content":"content 1","id":1},{"title":"title 2", "content":"content 2","id":2},{"title":"title 3", "content":"content 3","id":3},{"title":"title 4", "content":"content 4","id":4}]

def find_post(id):
      for p in my_posts:
            if p["id"]==id:
                  return p


@app.get("/")
async def root():
      return {"message": "to app"}


@app.post("/posts")
def create_posts(post:Post):
      post_dict=post.dict()
      post_dict['id'] = randrange(0,1000000)
      my_posts.append(post_dict)
      return {"data":post_dict}



@app.get("/posts")
def get_all_posts():
      return {"data":my_posts}

@app.get("/posts/{id}")
def get_posts(id: int):
      # print(id)
      post = find_post(int(id))
      return {"post details":post}


# @app.put("/posts/{id}")
# def update_posts():
#       return{}



# @app.delete("/posts/{id}")
# def delete_posts():
#       return {}