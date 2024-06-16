FROM python:3.11.9-alpine3.20

RUN mkdir /gradio
WORKDIR /gradio

# Used for manual testing
RUN apk add curl
# Installs GCC etc.
RUN apk add build-base
# Required for litellm
RUN apk add -u libffi-dev

# Ollama client used to connect to Ollama
RUN pip install ollama==0.2.1
# Used for connecting through an LLM through a UI build with Python code
RUN pip install gradio==4.36.1
# Used for connecting multiple LLMs and tools together
RUN pip install pyautogen==0.2.29
# Used as a proxy with Ollama so that Ollama can be queried using OpenAPI logic
RUN pip install 'litellm[proxy]'

