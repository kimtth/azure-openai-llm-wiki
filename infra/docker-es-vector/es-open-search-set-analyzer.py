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

es.indices.open(index=index_name)

# https://qiita.com/shin_hayata/items/41c07923dbf58f13eec4
index_settings = {
    "analysis": {
        "analyzer": {
            "my_ja_analyzer": {
                "type": "custom",
                "tokenizer": "kuromoji_tokenizer",
                "char_filter": [
                    "icu_normalizer",
                    "kuromoji_iteration_mark"
                ],
                "filter": [
                    "kuromoji_baseform",
                    "kuromoji_part_of_speech",
                    "ja_stop",
                    "kuromoji_number",
                    "kuromoji_stemmer"
                ]
            }
        }
    }
}

index_settings = {
    "analysis": {
        "analyzer": {
            "my_ja_analyzer2": {
                "type": "custom",
                "char_filter": [
                    "icu_normalizer"
                ],
                "tokenizer": "kuromoji_tokenizer",
                "filter": [
                    "kuromoji_baseform",
                    "kuromoji_part_of_speech",
                    "cjk_width",
                    "ja_stop",
                    "kuromoji_stemmer",
                    "lowercase"
                ]
            }
        }
    }
}

es.indices.close(index=index_name)
es.indices.put_settings(index=index_name, body=index_settings)
es.indices.open(index=index_name)
# text_field = "content"
#
# mapping = {
#     "properties": {
#         text_field: {
#             "type": "text",
#             "analyzer": "my_ja_analyzer"
#         }
#     }
# }
# es.indices.put_mapping(index=index_name, body=mapping)
