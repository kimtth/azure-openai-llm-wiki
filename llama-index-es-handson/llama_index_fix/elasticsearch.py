"""Elasticsearch/Opensearch vector store."""
import json
from typing import Any, Dict, List, Optional

from llama_index.data_structs import Node
from llama_index.vector_stores.types import (
    NodeEmbeddingResult,
    VectorStore,
    VectorStoreQueryResult,
)

class ElasticsearchVectorClient:

    def __init__(
        self,
        endpoint: str,
        index: str,
        dim: int,
        embedding_field: str = "embedding",
        text_field: str = "content",
        method: Optional[dict] = None,
        auth: Optional[dict] = None
    ):
        """Init params."""
        if method is None:
            method = "cosine"
        import_err_msg = "`httpx` package not found, please run `pip install httpx`"
        if embedding_field is None:
            embedding_field = "embedding"
        try:
            import httpx  # noqa: F401
        except ImportError:
            raise ImportError(import_err_msg)
        self._embedding_field = embedding_field

        if auth is None:
            self._client = httpx.Client(base_url=endpoint)
        else:
            if not 'verify' in auth:
                # Dev/Test Dokcer image requires SSL verification when accessing with HTTPS, https://localhost:9200.
                auth['verify'] = False
            if not 'basic_auth' in auth:
                # Please note that 'admin:admin' is the default username/password for the Opensearch image.
                auth['basic_auth'] = ("admin", "admin")
            self._client = httpx.Client(base_url=endpoint, verify= auth['verify'], auth=auth['basic_auth'])

        self._endpoint = endpoint
        self._dim = dim
        self._index = index
        self._text_field = text_field
        # initialize mapping
        idx_conf = {
            "mappings": {
                "properties": {
                    embedding_field: {
                        "type": "dense_vector",
                        "dims": dim,
                        "index": True,
                        "similarity": method,
                    },
                }
            },
        }
        #
        '''
        (Required, integer) Number of vector dimensions. 
        Can’t exceed 1024 for indexed vectors ("index": true), or 2048 for non-indexed vectors.
        '''
        res = self._client.put(f"/{self._index}", json=idx_conf)
        # will 400 if the index already existed, so allow 400 errors right here
        assert res.status_code == 200 or res.status_code == 400

    def index_results(self, results: List[NodeEmbeddingResult]) -> List[str]:
        """Store results in the index."""
        bulk_req: List[Dict[Any, Any]] = []
        for result in results:
            bulk_req.append({"index": {"_index": self._index, "_id": result.id}})
            bulk_req.append(
                {
                    self._text_field: result.node.text,
                    self._embedding_field: result.embedding,
                }
            )
        bulk = "\n".join([json.dumps(v) for v in bulk_req]) + "\n"
        res = self._client.post(
            "/_bulk", headers={"Content-Type": "application/x-ndjson"}, content=bulk
        )
        assert res.status_code == 200
        assert not res.json()["errors"], "expected no errors while indexing docs"
        return [r.id for r in results]

    def delete_doc_id(self, doc_id: str) -> None:
        """Delete a document.

        Args:
            doc_id (str): document id
        """
        self._client.delete(f"{self._index}/_doc/{doc_id}")

    def do_approx_knn(
        self, query_embedding: List[float], k: int
    ) -> VectorStoreQueryResult:
        """Do approximate knn."""
        res = self._client.post(
            f"{self._index}/_search",
            json={
                "knn": {
                    "field": self._embedding_field,
                    "query_vector": query_embedding,
                    "k": k,
                    "num_candidates": 100
                }
            },
        )
        nodes = []
        ids = []
        scores = []
        for hit in res.json()["hits"]["hits"]:
            source = hit["_source"]
            text = source[self._text_field]
            doc_id = hit["_id"]
            node = Node(text=text, extra_info=source, doc_id=doc_id)
            ids.append(doc_id)
            nodes.append(node)
            scores.append(hit["_score"])
        return VectorStoreQueryResult(nodes=nodes, ids=ids, similarities=scores)


class ElasticsearchVectorStore(VectorStore):
    """Elasticsearch/Opensearch vector store.

    Args:
        client (OpensearchVectorClient): Vector index client to use
            for data insertion/querying.

    """

    stores_text: bool = True

    def __init__(
        self,
        client: ElasticsearchVectorClient,
    ) -> None:
        """Initialize params."""
        import_err_msg = "`httpx` package not found, please run `pip install httpx`"
        try:
            import httpx  # noqa: F401
        except ImportError:
            raise ImportError(import_err_msg)
        self._client = client

    @property
    def client(self) -> Any:
        """Get client."""
        return self._client

    @property
    def config_dict(self) -> dict:
        """Get config dict."""
        return {}

    def add(
        self,
        embedding_results: List[NodeEmbeddingResult],
    ) -> List[str]:
        """Add embedding results to index.

        Args
            embedding_results: List[NodeEmbeddingResult]: list of embedding results

        """
        self._client.index_results(embedding_results)
        return [result.id for result in embedding_results]

    def delete(self, doc_id: str, **delete_kwargs: Any) -> None:
        """Delete a document.

        Args:
            doc_id (str): document id

        """
        self._client.delete_doc_id(doc_id)

    def query(
        self,
        query_embedding: List[float],
        similarity_top_k: int,
        doc_ids: Optional[List[str]] = None,
        query_str: Optional[str] = None,
    ) -> VectorStoreQueryResult:
        """Query index for top k most similar nodes.

        Args:
            query_embedding (List[float]): query embedding
            similarity_top_k (int): top k most similar nodes

        """
        return self._client.do_approx_knn(query_embedding, similarity_top_k)
