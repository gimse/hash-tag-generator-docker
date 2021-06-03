from fastapi import FastAPI
from hashtag.HashTagGenerator import generateHashtag

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/v1/hashtags")
async def read_item(text: str):
    return generateHashtag(text)