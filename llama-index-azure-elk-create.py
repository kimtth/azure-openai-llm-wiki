import os
from os import getenv

import openai
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import AzureOpenAI
from llama_index import SimpleDirectoryReader, PromptHelper, ServiceContext, LangchainEmbedding, LLMPredictor
from llama_index.indices.vector_store import GPTOpensearchIndex
from llama_index.vector_stores import OpensearchVectorClient
from llama_index_fix.elasticsearch import ElasticsearchVectorClient, ElasticsearchVectorStore
from llama_index_fix.vector_indices import GPTElasticsearchIndex
from settings import Settings

# Using as a vector index.

# http endpoint for your cluster (opensearch required for vector index usage)

env = Settings.config()
print(env['OPENAI_API_TYPE'])

openai.api_type = env['OPENAI_API_TYPE']
openai.api_base = env['OPENAI_API_BASE']
openai.api_version = env['OPENAI_API_VERSION'] # 2023-03-15-preview
os.environ['OPENAI_API_KEY'] = env['OPENAI_API_KEY']
openai.api_key = os.getenv("OPENAI_API_KEY")

llm = AzureOpenAI(deployment_name=env['OPENAI_DEPLOYMENT_NAME_A'], model_kwargs={
    "api_key": openai.api_key,
    "api_base": openai.api_base,
    "api_type": openai.api_type,
    "api_version": openai.api_version,
})
llm_predictor = LLMPredictor(llm=llm)

embedding_llm = LangchainEmbedding(OpenAIEmbeddings(
    document_model_name=env['OPENAI_DOCUMENT_MODEL_NAME'],
    query_model_name=env['OPENAI_QUERY_MODEL_NAME'],
    chunk_size=1
))

# "query_prompt_helper = PromptHelper(4096, 256, 0)
prompt_helper = PromptHelper.from_llm_predictor(llm_predictor)

service_context = ServiceContext.from_defaults(
    llm_predictor=llm_predictor,
    embed_model=embedding_llm,
    prompt_helper=prompt_helper
)

# load some sample data
documents = SimpleDirectoryReader('files').load_data()

# Index to demonstrate the VectorStore impl
endpoint = getenv("OPENSEARCH_ENDPOINT", "http://localhost:9200/")
idx = getenv("OPENSEARCH_INDEX", env['INDEX_NAME'])

# OpensearchVectorClient stores text in this field by default
text_field = env['INDEX_TEXT_FIELD']
# OpensearchVectorClient stores embeddings in this field by default
embedding_field = env['INDEX_EMBEDDING_FIELD']

# OpensearchVectorClient encapsulates logic for a single opensearch index with vector search enabled
auth_info = {
    'basic_auth': (env['ELASTIC_SEARCH_ID'], env['ELASTIC_SEARCH_PASSWORD'])
}
# dim=1536 -> !Must: 1536 is the predefined value.
'''
: from open ai documents
text-embedding-ada-002: 
Smaller embedding size. The new embeddings have only 1536 dimensions, one-eighth the size of davinci-001 embeddings, 
making the new embeddings more cost effective in working with vector databases. 
https://openai.com/blog/new-and-improved-embedding-model

: from open search documents
However, one exception to this is that the maximum dimension count for the Lucene engine is 1,024, compared with
16,000 for the other engines. https://opensearch.org/docs/latest/search-plugins/knn/approximate-knn/

: from llama-index examples
However, the examples in llama-index use 1536 vector size.
'''
client = ElasticsearchVectorClient(endpoint, idx, 1536, embedding_field=embedding_field, text_field=text_field,
                                auth=auth_info)
index = GPTElasticsearchIndex.from_documents(documents=documents, client=client, service_context=service_context)

index.save_to_disk('index.json')
