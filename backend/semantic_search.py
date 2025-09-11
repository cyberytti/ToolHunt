from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import BM25Retriever
import pandas as pd

class SemanticSearch:
    """
    A class to perform semantic search on a list of tools.
    It uses a hybrid approach with BM25 and FAISS to get the best of both worlds:
    - BM25 for keyword-based search.
    - FAISS for semantic similarity search.
    """
    def __init__(self, data_path='backend/database/tool_list_database.csv'):
        """
        Initializes the SemanticSearch object.
        - Loads the tool data from the CSV file.
        - Initializes the HuggingFace embeddings model.
        - Creates the BM25 and FAISS retrievers.
        """
        # Load the sentence transformer model for embeddings
        self.embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        
        # Load the tool data from the CSV file
        self.df = pd.read_csv(data_path)
        self.df.fillna('', inplace=True)
        print(f"Loaded {len(self.df)} rows")

        # Create a list of documents for the retrievers
        self.doc_list = (self.df['name'] + ' ' + self.df['description']).tolist()
        
        # Initialize the BM25 retriever for keyword-based search
        self.bm25_retriever = BM25Retriever.from_texts(self.doc_list)

        # Initialize the FAISS vector store and retriever for semantic search
        self.faiss_vectorstore = FAISS.from_texts(self.doc_list, self.embedding)
        self.faiss_retriever = self.faiss_vectorstore.as_retriever(search_kwargs={"k": 20})

    def search(self, query, similarity_threshold=0.5):
        """
        Performs a hybrid search using BM25 and FAISS.
        - Gets the results from the FAISS retriever.
        - Filters the FAISS results based on a similarity threshold.
        - Gets the results from the BM25 retriever.
        - Combines the results from both retrievers, giving priority to the FAISS results.
        """
        # Get the semantic search results from FAISS
        faiss_results = self.faiss_retriever.invoke(query)
        
        # Filter the FAISS results based on the similarity threshold
        filtered_results = []
        for doc in faiss_results:
            # The distance score from FAISS is converted to a similarity score
            distance = doc.metadata.get('score', 0) if 'score' in doc.metadata else 0
            similarity = 1 - distance
            
            if similarity >= similarity_threshold:
                filtered_results.append(doc)
        
        # Get the keyword-based search results from BM25
        bm25_results = self.bm25_retriever.invoke(query)
        
        # Combine the results from both retrievers
        unique_results = {}
        
        # Add the filtered FAISS results first
        for doc in filtered_results:
            unique_results[doc.page_content] = doc
        
        # Add the BM25 results, avoiding duplicates
        for doc in bm25_results[:10]:  # Limit the number of BM25 results
            if doc.page_content not in unique_results:
                unique_results[doc.page_content] = doc
        
        return list(unique_results.keys())