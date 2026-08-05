from langchain_qdrant import QdrantVectorStore

from qdrant_client import QdrantClient


class QdrantManager:

    def __init__(
            self,
            collection,
            path,
            embeddings
    ):

        self.client = QdrantClient(
            path=path
        )

        self.collection = collection

        self.embeddings = embeddings

    def create_store(self, documents):

        return QdrantVectorStore.from_documents(
            documents,
            embedding=self.embeddings,
            path="./qdrant_db",
            collection_name=self.collection
        )

    def close(self):

        self.client.close()