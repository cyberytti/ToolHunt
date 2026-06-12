from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import BM25Retriever

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")
FAISS_INDEX_PATH = Path(__file__).resolve().parent / "faiss_index"


def build_or_load_faiss_index(doc_list, force_rebuild=False):
    if FAISS_INDEX_PATH.exists() and not force_rebuild:
        print("Loading FAISS index from disk...")
        vectorstore = FAISS.load_local(
            str(FAISS_INDEX_PATH),
            embedding,
            allow_dangerous_deserialization=True,
        )
    else:
        print("Building FAISS index...")
        vectorstore = FAISS.from_texts(doc_list, embedding)
        vectorstore.save_local(str(FAISS_INDEX_PATH))
    return vectorstore


def search(doc_list, query, similarity_threshold=0.5):
    # Create retrievers
    bm25_retriever = BM25Retriever.from_texts(doc_list)
    faiss_vectorstore = build_or_load_faiss_index(doc_list)

    # Get FAISS results with raw distances and normalize them into a stable 0-1 similarity.
    faiss_results = faiss_vectorstore.similarity_search_with_score(query, k=198)

    # Filter FAISS results by similarity threshold.
    filtered_results = []
    for doc, distance in faiss_results:
        similarity = 1 / (1 + distance)
        if similarity >= similarity_threshold:
            filtered_results.append(doc)

    # Get BM25 results (retrievers now use invoke in current LangChain versions).
    bm25_results = bm25_retriever.invoke(query)
    
    # Combine results (you can implement your own ensemble logic here)
    # For now, let's prioritize FAISS results above threshold, then BM25
    unique_results = {}
    
    # Add filtered FAISS results first
    for doc in filtered_results:
        unique_results[doc.page_content] = doc
    
    # Add BM25 results (you might want to limit these too)
    for doc in bm25_results:
        if doc.page_content not in unique_results:
            unique_results[doc.page_content] = doc
    
    return list(unique_results.keys())
