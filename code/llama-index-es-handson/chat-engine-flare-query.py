import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from llama_index.query_engine import FLAREInstructQueryEngine
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    LLMPredictor,
    ServiceContext,
)

service_context = ServiceContext.from_defaults(
    # llm_predictor=LLMPredictor(llm=ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)),
    llm_predictor=LLMPredictor(llm=ChatOpenAI(model_name='gpt-4', temperature=0)),
    chunk_size=512
)

documents = SimpleDirectoryReader("../data/paul_graham").load_data()
index = VectorStoreIndex.from_documents(documents, service_context=service_context)

index_query_engine = index.as_query_engine(similarity_top_k=2)

flare_query_engine = FLAREInstructQueryEngine(
    query_engine=index_query_engine,
    service_context=service_context,
    max_iterations=7,
    verbose=True
)

response = flare_query_engine.query("Can you tell me about the author's trajectory in the startup world?")

print(response)

response = flare_query_engine.query("Can you tell me about what the author did during his time at YC?")

print(response)