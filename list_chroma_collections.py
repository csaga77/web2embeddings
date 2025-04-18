import chromadb

def list_collections():
    # Connect to the Chroma database located at artifacts/vector_stores/chroma_db
    client = chromadb.PersistentClient(path="/Users/bchen/Workspace/web2embeddings/artifacts/vector_stores/chroma_db")

    # Retrieve the list of collections
    collections = client.list_collections()

    # Print the collections
    for collection in collections:
        print(collection)

if __name__ == "__main__":
    list_collections()
