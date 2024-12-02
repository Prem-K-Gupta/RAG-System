from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(data):
    return model.encode(data, convert_to_tensor=True)
