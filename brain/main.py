import openai
import os
from fastapi import FastAPI

openai.api_key = os.getenv('OPENAPI_KEY')

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/question/")
def question(json: dict):
    question = json.get("question")
    system = '''
        あなたはバーチャルYouTuberです。
        現在YouTubeでライブ配信をしており、視聴者と適切な対話を行う必要があります。
        視聴者からの質問に30から200文字程度で適切に応答してください。
    '''
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": f"{question}"}])
    ans = response["choices"][0]["message"]["content"]
    return {"answer": ans}
