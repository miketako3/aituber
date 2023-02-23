import os
import pytchat
from fastapi import FastAPI

app = FastAPI()
VIDEO_ID = os.getenv("VIDEO_ID")
livechat = pytchat.create(video_id=VIDEO_ID)


@app.get("/hear")
def hear():
    chat = livechat.get()
    try:
        return {"chat": chat.items[-1].message}
    except:
        return {"chat": ""}
