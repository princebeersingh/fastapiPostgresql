from fastapi import FastAPI
from fastapi.params import Body


app =FastAPI()

@app.get("/")
async def root():
      return {"message": "to app"}

@app.get("/posts")
def get_posts():
      return {"data": "this is your post"}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
      
      return {"new post":f"title : {payLoad['title']}, content : {payLoad['content']}"}