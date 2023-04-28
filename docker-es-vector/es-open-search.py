from opensearchpy import OpenSearch

host = 'localhost'
port = 9200
auth_user = "admin"
auth_pwd = "admin"
es = OpenSearch(
    hosts=[{'host': host, 'port': port}],
    use_ssl=True,
    http_auth=(auth_user, auth_pwd),
    verify_certs=False
)
index_name = "gpt-index-demo"

if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

es.create(index=index_name, id=1, body={"title": "Test", "content": "Test content"})