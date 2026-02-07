import chromadb

client = chromadb.Client()
collection = client.create_collection("documents")

def add_doc(doc_id, content):
    collection.add(
        documents=[content],
        ids=[doc_id]
    )
