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
    prompt = f'''
    あなたはバーチャルYouTuberです。
    現在YouTubeでライブ配信をしており、視聴者と適切な対話を行う必要があります。
    視聴者からの最新のコメントは次の通りです。30から200文字程度で適切に応答してください。
    「{question}」
    「
    '''
    ans = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
        frequency_penalty=0.5,
        echo=False,
        stop="」",
        best_of=3
    )
    return {"answer": ans["choices"][0]["text"]}
