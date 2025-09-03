from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import BM25Retriever


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")


def search(doc_list, query, similarity_threshold=0.5):
    # Create retrievers
    bm25_retriever = BM25Retriever.from_texts(doc_list)
    faiss_vectorstore = FAISS.from_texts(doc_list, embedding)
    faiss_retriever = faiss_vectorstore.as_retriever(search_kwargs={"k": 20})
    
    # Get results with scores
    faiss_results = faiss_retriever.get_relevant_documents(query)
    
    # Filter FAISS results by similarity threshold
    filtered_results = []
    for doc in faiss_results:
        # FAISS returns distance, convert to similarity
        # For cosine similarity: similarity = 1 - distance
        distance = doc.metadata.get('score', 0) if 'score' in doc.metadata else 0
        similarity = 1 - distance
        
        if similarity >= similarity_threshold:
            filtered_results.append(doc)
    
    # Get BM25 results (they don't have similarity scores in the same way)
    bm25_results = bm25_retriever.get_relevant_documents(query)
    
    # Combine results (you can implement your own ensemble logic here)
    # For now, let's prioritize FAISS results above threshold, then BM25
    unique_results = {}
    
    # Add filtered FAISS results first
    for doc in filtered_results:
        unique_results[doc.page_content] = doc
    
    # Add BM25 results (you might want to limit these too)
    for doc in bm25_results[:10]:  # Limit BM25 results
        if doc.page_content not in unique_results:
            unique_results[doc.page_content] = doc
    
    return list(unique_results.keys())
