FROM pytorch/pytorch

RUN mkdir /rag
WORKDIR /rag

#RUN apk update
# Installs GCC etc.
#RUN apk add build-base
# Needed for downloading data files
#RUN apk add wget
# Ollama client used to connect to Ollama
RUN pip install ollama==0.2.1
# Used for connecting through an LLM through a UI build with Python code
#RUN pip install gradio==4.36.1
# Used for RAG
RUN pip install llama_index
RUN pip install llama-index-llms-ollama
RUN pip install llama-index-embeddings-huggingface

# Required for llama-index-embeddings-huggingface
#RUN apk add curl
#RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
#RUN source "$HOME/.cargo/env"
#ENV PATH="${PATH}:/root/.cargo/bin:"
#ENV PYTHONPATH=/usr/local/
#RUN apk add pkgconfig
#RUN pip install huggingface_hub
