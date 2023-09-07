from typing import Any, Optional, Sequence, Type, cast

from llama_index.data_structs.data_structs_v2 import (
    IndexDict,
    OpensearchIndexDict,
)
from llama_index.data_structs.node_v2 import Node
from llama_index.indices.base import BaseGPTIndex, QueryMap
from llama_index.indices.query.schema import QueryMode

from llama_index.indices.service_context import ServiceContext
from llama_index.indices.vector_store.base import GPTVectorStoreIndex
from llama_index_fix.elasticsearch import ElasticsearchVectorStore, ElasticsearchVectorClient


class GPTElasticsearchIndex(GPTVectorStoreIndex):

    index_struct_cls: Type[IndexDict] = OpensearchIndexDict

    def __init__(
        self,
        nodes: Optional[Sequence[Node]] = None,
        service_context: Optional[ServiceContext] = None,
        client: Optional[ElasticsearchVectorClient] = None,
        index_struct: Optional[IndexDict] = None,
        **kwargs: Any,
    ) -> None:
        """Init params."""
        if client is None:
            raise ValueError("client is required.")
        vector_store = ElasticsearchVectorStore(client)
        super().__init__(
            nodes=nodes,
            index_struct=index_struct,
            service_context=service_context,
            vector_store=vector_store,
            **kwargs,
        )

    @classmethod
    def get_query_map(self) -> QueryMap:
        """Get query map."""
        return {
            QueryMode.DEFAULT: GPTOpensearchIndexQuery,
            QueryMode.EMBEDDING: GPTOpensearchIndexQuery,
        }

    def _preprocess_query(self, mode: QueryMode, query_kwargs: Any) -> None:
        """Preprocess query."""
        super()._preprocess_query(mode, query_kwargs)
        del query_kwargs["vector_store"]
        vector_store = cast(ElasticsearchVectorStore, self._vector_store)
        query_kwargs["client"] = vector_store._client