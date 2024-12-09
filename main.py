from fastapi import FastAPI, Response,status,HTTPException
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


@app.post("/posts",status_code=status.HTTP_201_CREATED)
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
      post = find_post(id)
      if not post:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id {id} not found")
            # response.status_code = status.HTTP_404_NOT_FOUND
            # return{"message":f"post with id {id} not found"}
      return {"post details":post}


# @app.put("/posts/{id}")
# def update_posts():
#       return{}

def find_post_index(id):
      for i, p in enumerate(my_posts):
            if p['id']==id:
                  return i
                  

@app.delete("/posts/{id}")
def delete_posts(id:int):
      index = find_post_index(id)
      if index==None:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id {id} doesn't exist!")
      my_posts.pop(index)
      return Response(status_code= status.HTTP_204_NO_CONTENT)