# Use reader to check out what GPTOpensearchIndex just created in our index.
from os import getenv

# create a reader to check out the index used in previous section.
from llama_index.readers import ElasticsearchReader

from settings import Settings

env = Settings.config()

index_name = env['INDEX_NAME']
# http endpoint for your cluster (opensearch required for vector index usage)
endpoint = getenv("OPENSEARCH_ENDPOINT", "https://localhost:9200")
# index to demonstrate the VectorStore impl
idx = getenv("OPENSEARCH_INDEX", index_name)

# OpensearchVectorClient stores text in this field by default
text_field = env['INDEX_TEXT_FIELD']
# OpensearchVectorClient stores embeddings in this field by default
embedding_field = env['INDEX_EMBEDDING_FIELD']

args = {
    "verify": False,
    "auth": (env['OPEN_SEARCH_ID'], env['OPEN_SEARCH_PASSWORD'])
}
rdr = ElasticsearchReader(endpoint, idx, httpx_client_args=args)
# set embedding_field optionally to read embedding data from the elasticsearch index
docs = rdr.load_data(text_field, embedding_field=embedding_field)
# docs have embeddings in them
print("embedding dimension:", len(docs[1].embedding))
# full document is stored in extra_info
print("all fields in index:", docs[0].extra_info.keys())

# we can check out how the text was chunked by the `GPTOpensearchIndex`
print("total number of chunks created:", len(docs))

# search index using standard elasticsearch query DSL
docs = rdr.load_data(text_field, {"query": {"match": {text_field: "マニュアル化"}}})
print("chunks that mention :", len(docs))
for doc in docs:
    print(doc.text)
docs = rdr.load_data(text_field, {"query": {"match": {text_field: "勤怠システム"}}})
print("chunks that mention :", len(docs))
for doc in docs:
    print(doc.text)

