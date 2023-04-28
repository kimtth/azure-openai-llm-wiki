import os
from os import getenv

import openai
from langchain import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import AzureOpenAI
from llama_index import LLMPredictor, GPTVectorStoreIndex, GPTSimpleVectorIndex, LangchainEmbedding, PromptHelper, \
    ServiceContext
from llama_index.indices.vector_store import GPTOpensearchIndex
from llama_index.node_parser import SimpleNodeParser
from llama_index.readers import ElasticsearchReader
from llama_index.vector_stores import OpensearchVectorClient

from settings import Settings

env = Settings.config()
print(env['OPENAI_API_TYPE'])

text_field = env['INDEX_TEXT_FIELD']
embedding_field = env['INDEX_EMBEDDING_FIELD']
index_name = env['INDEX_NAME']

endpoint = getenv("OPENSEARCH_ENDPOINT", "https://localhost:9200")
# index to demonstrate the VectorStore impl
idx = getenv("OPENSEARCH_INDEX", index_name)

args = {
    "verify": False,
    "auth": (env['OPEN_SEARCH_ID'], env['OPEN_SEARCH_PASSWORD'])
}

openai.api_type = env['OPENAI_API_TYPE']
openai.api_base = env['OPENAI_API_BASE']
openai.api_version = env['OPENAI_API_VERSION'] # 2023-03-15-preview
os.environ['OPENAI_API_KEY'] = env['OPENAI_API_KEY']
openai.api_key = os.getenv("OPENAI_API_KEY")

llm = AzureOpenAI(deployment_name=env['OPENAI_DEPLOYMENT_NAME_C'], model_name="text-davinci-003", model_kwargs={
    "api_key": openai.api_key,
    "api_base": openai.api_base,
    "api_type": openai.api_type,
    "api_version": openai.api_version,
})
llm_predictor = LLMPredictor(llm=llm)
# llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003"))

# https://learn.microsoft.com/en-us/answers/questions/1189176/how-do-i-resolve-error-deploymentnotfound-for-azure
'''
# openai.error.InvalidRequestError: The API deployment for this resource does not exist.
# If you created the deployment within the last 5 minutes, please wait a moment and try again.

-> I resolved the issue by removing hyphens from the deployment name. 
The problem is that the model deployment name create prompt in Azure OpenAI, Model Deployments states that '-', '', and '.' are allowed.
However, when you create the deployment name in the OpenAI Studio, the create prompt does not allow '-', '', and '.' . 
This is inconsistent between the two different methods to create a deployment name.
'''
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
auth_info = {
    'basic_auth': (env['OPEN_SEARCH_ID'], env['OPEN_SEARCH_PASSWORD'])
}

client = OpensearchVectorClient(endpoint, idx, 1536, embedding_field=embedding_field, text_field=text_field,
                                auth=auth_info)
rdr = ElasticsearchReader(endpoint, idx, httpx_client_args=args)
documents = rdr.load_data(field=text_field, embedding_field=embedding_field)

parser = SimpleNodeParser()
# To use include_extra_info, the parameter should access through node parser.
nodes = parser.get_nodes_from_documents(documents, include_extra_info=False)
index = GPTOpensearchIndex(nodes=nodes, client=client, service_context=service_context)
# index = GPTSimpleVectorIndex(nodes=nodes, service_context=service_context)

query_str = "働き方改革とは?"
query_str = "働き方改革で、残業時間が減り、気持ちに余裕ができました事例を教えて"
answer = index.query(query_str)
# print(answer.get_formatted_sources())
print('query was:', query_str)
print('answer was:', str(answer).strip())

'''
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total LLM token usage: 0 tokens
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total embedding token usage: 0 tokens

query was: 働き方改革で、残業時間が減り、気持ちに余裕ができました事例を教えて
answer was: 一例として、働き方改革を実施した小規模事業者の事例を紹介します。
当事業者は、残業時間に関する原則を採用し、月45時間を超える残業を行うことを禁止し、月80時間の上限を設けました。
また、同一企業内において、正社員と非正規雇用労働者との間で、基本給や賞与などのあらゆる待遇について、不合理な待遇差を設けることを
 
INFO:llama_index.token_counter.token_counter:> [query] Total LLM token usage: 35896 tokens
INFO:llama_index.token_counter.token_counter:> [query] Total embedding token usage: 58 tokens
'''

