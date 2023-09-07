from elasticsearch import Elasticsearch

# To Opensearch, Elasticsearch API does not work.
# elasticsearch.UnsupportedProductError:
# The client noticed that the server is not Elasticsearch and we do not support this unknown product.

auth_user = "admin"
auth_pwd = "admin"
es = Elasticsearch(
    hosts='https://localhost:9200/',
    basic_auth=(auth_user, auth_pwd),
    verify_certs=False
)
index_name = "gpt-index-demo"

print(es.indices.exists(index=index_name))

es.indices.create(index=index_name)

# Starter
# Indexing a document
es.create(index=index_name, id=1, body={"title": "Test", "content": "Test content"})
#
# # Getting a document
# es.get(index="my-index", id=1)
#
# # Refreshing an index
# es.indices.refresh(index="my-index")
#
# # Searching for a document
# es.search(index="my-index", body={"query": {"match_all": {}}})
#
# # Updating a document
# es.update(index="my-index", id=1, body={"doc": {"title": "Updated title"}})
#
# # Deleting a document
# es.delete(index="my-index", id=1)

# Vector search

embedding_field = "embedding"

query = {
    "query": {
        "script_score": {
            "query": {
                "match_all": {}
            },
            "script": {
                "source": "cosineSimilarity(params.queryVector, 'vector_field')"
            },
            "params": {
                "queryVector": [1, 2, 3]
            }
        }
    }
}
result = es.search(index=index_name, body=query)

