from elasticsearch import Elasticsearch

auth_user = "admin"
auth_pwd = "admin"
es = Elasticsearch(
    hosts='https://localhost:9200/',
    basic_auth=(auth_user, auth_pwd),
    verify_certs=False
)

index_name = "gpt-index-demo"

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

es.indices.put_settings(index=index_name, settings=index_settings)
text_field = "content"

mapping = {
    "properties": {
        text_field: {
            "type": "text",
            "analyzer": "my_ja_analyzer"
        }
    }
}
es.indices.put_mapping(index=index_name, body=mapping)
