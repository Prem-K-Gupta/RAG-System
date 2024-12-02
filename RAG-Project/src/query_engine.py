from embeddings import generate_embeddings
from database import search_database

def handle_query(query, collection):
    query_vector = generate_embeddings(query)
    results = search_database(collection, query_vector)
    return results
