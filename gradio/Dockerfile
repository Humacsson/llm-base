FROM python:3.11.9-alpine3.20

RUN mkdir /gradio
WORKDIR /gradio

RUN apk add curl
RUN apk add build-base

RUN pip install ollama==0.2.1 gradio==4.36.1

CMD ["python", "run.py"]

