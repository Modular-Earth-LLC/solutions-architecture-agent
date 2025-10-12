# Setup Vector Database for RAG

**Agent:** Knowledge Engineering Agent  
**Category:** Knowledge Engineering  
**Complexity:** Advanced  
**Duration:** 2-4 hours

---

## Purpose

Set up a vector database (ChromaDB or FAISS) with document ingestion pipeline for RAG (Retrieval-Augmented Generation) systems.

---

## Instructions

Implement vector database with:

1. **Vector store selection** (ChromaDB for persistence, FAISS for performance)
2. **Embedding model configuration** (AWS Bedrock Titan or local)
3. **Document ingestion pipeline**
4. **Text chunking strategy**
5. **Retriever interface for LangChain**

---

## Expected Output

```python
# src/knowledge/vectorstore.py

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import BedrockEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
import chromadb
import os

class VectorStoreManager:
    """Manage vector database for RAG"""
    
    def __init__(
        self,
        collection_name: str = "knowledge_base",
        persist_directory: str = "./chroma_db"
    ):
        self.collection_name = collection_name
        self.persist_directory = persist_directory
        
        # Initialize embeddings
        self.embeddings = BedrockEmbeddings(
            model_id="amazon.titan-embed-text-v1",
            region_name=os.getenv("AWS_REGION", "us-east-1")
        )
        
        # Initialize ChromaDB
        self.client = chromadb.PersistentClient(path=persist_directory)
        
        self.vectorstore = Chroma(
            client=self.client,
            collection_name=collection_name,
            embedding_function=self.embeddings
        )
    
    def ingest_documents(
        self,
        source_dir: str,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ) -> int:
        """Ingest documents from directory"""
        
        # Load documents
        loader = DirectoryLoader(
            source_dir,
            glob="**/*.txt",
            loader_cls=TextLoader
        )
        documents = loader.load()
        
        # Split into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
        )
        splits = text_splitter.split_documents(documents)
        
        # Add to vector store
        self.vectorstore.add_documents(splits)
        
        return len(splits)
    
    def get_retriever(self, k: int = 5):
        """Get retriever for LangChain"""
        return self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": k}
        )
    
    def search(self, query: str, k: int = 5):
        """Semantic search"""
        results = self.vectorstore.similarity_search_with_score(
            query=query,
            k=k
        )
        return results

# Usage
if __name__ == "__main__":
    manager = VectorStoreManager()
    
    # Ingest documents
    count = manager.ingest_documents("./documents")
    print(f"Ingested {count} chunks")
    
    # Search
    results = manager.search("What is the return policy?")
    for doc, score in results:
        print(f"Score: {score}")
        print(f"Content: {doc.page_content[:200]}...")
```

---

## Success Criteria

✅ Vector database initialized  
✅ Documents ingested successfully  
✅ Semantic search returns relevant results  
✅ Retriever ready for LangChain integration  
✅ Persistence works across restarts

---

## Integration

**Provides To:**
- LangChain Agent (retriever for RAG chains)

**Next Steps:**
- Use LangChain Agent to build RAG chain
- Integrate with Streamlit UI for document Q&A
