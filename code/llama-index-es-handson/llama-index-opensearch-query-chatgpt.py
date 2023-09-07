import os
from os import getenv

import openai
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

openai.api_type = env['OPENAI_API_TYPE']
openai.api_base = env['OPENAI_API_BASE']
openai.api_version = "2023-03-15-preview"
os.environ['OPENAI_API_KEY'] = env['OPENAI_API_KEY']
openai.api_key = os.getenv("OPENAI_API_KEY")

# Not working for the following message. Langchain seems to not support chatGPT in Azure yet.
# openai.error.InvalidRequestError: logprobs, best_of and echo parameters are not available on gpt-35-turbo model.
# Please remove the parameter and try again.
llm = AzureOpenAI(deployment_name=env['OPENAI_DEPLOYMENT_NAME_B'], model_name="gpt-35-turbo", model_kwargs={
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

-> I resolved the issue by removing hyphens from the deployment name. The problem is that the model deployment name 
create prompt in Azure OpenAI, Model Deployments states that '-', '', and '.' are allowed. However, when you create 
the deployment name in the OpenAI Studio, the create prompt does not allow '-', '', and '.' . This is inconsistent 
between the two different methods to create a deployment name.'''
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
answer = index.query(query_str)
print(answer.get_formatted_sources())
print('query was:', query_str)
print('answer was:', str(answer).strip())
