import openai

openai.api_key = " "

def generate_response(query, context):
    prompt = f"Context: {context}\nUser Query: {query}\nResponse:"
    response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=150)
    return response["choices"][0]["text"]
