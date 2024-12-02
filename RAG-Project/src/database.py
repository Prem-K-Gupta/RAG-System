from pymilvus import Collection, connections

connections.connect(host="localhost", port="19530")

def create_collection(name):
    return Collection(name)

def insert_embeddings(collection, embeddings, metadata):
    collection.insert([embeddings, metadata])

def search_database(collection, query_vector, top_k=5):
    return collection.search(query_vector, "field", top_k=top_k)
