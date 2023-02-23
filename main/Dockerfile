FROM python:3.9-slim

WORKDIR /app

RUN apt update -y && apt install gcc libasound2-dev pulseaudio -y

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./ .

CMD ["python", "main.py"]