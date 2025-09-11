from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import BM25Retriever
import pandas as pd

class SemanticSearch:
    def __init__(self, data_path='backend/database/tool_list_database.csv'):
        self.embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.df = pd.read_csv(data_path)
        self.df.fillna('', inplace=True)
        print(f"Loaded {len(self.df)} rows")
        self.doc_list = (self.df['name'] + ' ' + self.df['description']).tolist()
        
        self.bm25_retriever = BM25Retriever.from_texts(self.doc_list)
        self.faiss_vectorstore = FAISS.from_texts(self.doc_list, self.embedding)
        self.faiss_retriever = self.faiss_vectorstore.as_retriever(search_kwargs={"k": 20})

    def search(self, query, similarity_threshold=0.5):
        faiss_results = self.faiss_retriever.invoke(query)
        
        filtered_results = []
        for doc in faiss_results:
            distance = doc.metadata.get('score', 0) if 'score' in doc.metadata else 0
            similarity = 1 - distance
            
            if similarity >= similarity_threshold:
                filtered_results.append(doc)
        
        bm25_results = self.bm25_retriever.invoke(query)
        
        unique_results = {}
        
        for doc in filtered_results:
            unique_results[doc.page_content] = doc
        
        for doc in bm25_results[:10]:
            if doc.page_content not in unique_results:
                unique_results[doc.page_content] = doc
        
        return list(unique_results.keys())