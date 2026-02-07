from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

class MultiModalVectorStore:
    def __init__(self):
        self.client = QdrantClient(":memory:")
        self.client.recreate_collection(
            collection_name="multimodal_docs",
            vectors_config={"size": 384, "distance": "Cosine"},
        )

    def add(self, vector, payload):
        self.client.upsert(
            collection_name="multimodal_docs",
            points=[
                PointStruct(
                    id=payload["id"],
                    vector=vector.tolist(),
                    payload=payload
                )
            ]
        )
