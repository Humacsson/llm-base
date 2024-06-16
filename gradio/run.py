import os

import gradio as gr
import ollama

client = ollama.Client(host="http://host.docker.internal:11434")

def generate_response(question):
    response = client.chat(model=model_name, messages=[
        {'role': 'system', 'content': prompt },
        {'role': 'user', 'content': question}
    ])
    return response['message']['content']

GR_ARGS = {
    'fn':generate_response,
    'inputs':"text",
    'outputs':"text",
    'title':"Gradio Prompt Testing",
    'description':"Chat with your model and prompt file of choice. The model will not remember your conversation, every message starts from scratch."
}

model_name = os.environ['LLM_BASE_GRADIO__OLLAMA_MODEL']
prompt = ""
with open(os.environ['LLM_BASE_GRADIO__PROMPT_FILE'], 'r') as file:
    prompt = file.read()

demo = gr.Interface(**GR_ARGS)

if __name__ == "__main__":
    print("Real URL is: http://localhost:7860")
    demo.launch(server_name="0.0.0.0")


