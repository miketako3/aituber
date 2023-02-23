import json
import requests
import simpleaudio as sa
import time

BRAIN_URL = "http://brain/question"
EAR_URL = "http://ear/hear"
VOICE_URL = "http://voice:50021"

while True:
    print("loop start")
    time.sleep(10)
    chat = requests.get(EAR_URL).json()["chat"]
    # ans = requests.post(BRAIN_URL, json={"question": chat}).json()["answer"]
    ans = "やったー"
    print(f'「{chat}」「 {ans}」', flush=True)
    params = {"text": ans, "speaker": 1}
    voice_request = requests.post(f"{VOICE_URL}/audio_query", params=params).json()
    print(voice_request, flush=True)
    voice = requests.post(f"{VOICE_URL}/synthesis", params={"speaker": 1}, data=json.dumps(voice_request)).content
    # with tempfile.TemporaryDirectory() as tmp:
    #     with open(f"{tmp}/output.wav", "wb") as f:
    #         f.write(voice)
    #         wave_object = sa.WaveObject.from_wave_file(f"{tmp}/output.wav")
    #         play_object = wave_object.play()
    #         play_object.wait_done()
    with open("./output.wav", "wb") as f:
        f.write(voice)
        wave_object = sa.WaveObject.from_wave_file("./output.wav")
        play_object = wave_object.play()
        play_object.wait_done()
