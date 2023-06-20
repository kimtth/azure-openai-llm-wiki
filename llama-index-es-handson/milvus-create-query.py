import logging
import sys

# Uncomment to see debug logs
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index import VectorStoreIndex, SimpleDirectoryReader, Document
from llama_index.vector_stores import MilvusVectorStore
from IPython.display import Markdown, display
import textwrap

import os
os.environ["OPENAI_API_KEY"] = "sk-"

vector_store = MilvusVectorStore(overwrite=False)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
query_engine = index.as_query_engine()
res = query_engine.query("What is the number?")
print("Res:", res)
