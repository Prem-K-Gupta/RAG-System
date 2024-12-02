import streamlit as st
from src.database import create_collection
from src.query_engine import handle_query
from src.response_gen import generate_response

collection_name = "knowledge_base"
collection = create_collection(collection_name)

st.title("RAG System for MES Knowledge Base")

query = st.text_input("Enter your query:")

if st.button("Search"):
    results = handle_query(query, collection)
    context = " ".join([res['text'] for res in results])

    response = generate_response(query, context)

    st.subheader("Generated Response:")
    st.write(response)

    st.subheader("Relevant Documents:")
    for res in results:
        st.write(f"- {res['text']} (Source: {res['metadata']})")
