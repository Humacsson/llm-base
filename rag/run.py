from llama_index.core import SimpleDirectoryReader
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex
from llama_index.core import SummaryIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

Settings.llm = Ollama(model='mistral:instruct', request_timeout=60.0)
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

docs = SimpleDirectoryReader(
    input_dir="data/", # Load all files in the data folder
    required_exts=['.pdf'], # Load only files with these extensions
    recursive=True # Load files in folders as well
).load_data()

vector_index = VectorStoreIndex.from_documents(docs)
vector_query_engine = vector_index.as_query_engine(similarity_top_k=2)

response = uber_vector_query_engine.query("What is the revenue of uber in 2021 in millions?")

print(response)
