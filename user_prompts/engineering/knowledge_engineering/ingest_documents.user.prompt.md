# Ingest Documents into Vector Database

**Agent:** Knowledge Engineering Agent  
**Category:** Knowledge Engineering  
**Complexity:** Intermediate  
**Duration:** 1-2 hours

---

## Purpose

Build document ingestion pipeline that loads, chunks, and indexes documents into vector database for RAG systems.

---

## Instructions

Create ingestion pipeline with:

1. **Document loaders** (PDF, TXT, MD, CSV)
2. **Text chunking strategy**
3. **Metadata extraction**
4. **Batch processing**
5. **Progress tracking**

---

## Expected Output

```python
# src/knowledge/ingest.py

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    UnstructuredMarkdownLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from pathlib import Path
from tqdm import tqdm

class DocumentIngestionPipeline:
    """Ingest documents into vector database"""
    
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
    
    def load_document(self, file_path: str):
        """Load single document based on file type"""
        path = Path(file_path)
        
        if path.suffix == '.pdf':
            loader = PyPDFLoader(str(path))
        elif path.suffix == '.txt':
            loader = TextLoader(str(path))
        elif path.suffix == '.md':
            loader = UnstructuredMarkdownLoader(str(path))
        elif path.suffix == '.csv':
            loader = CSVLoader(str(path))
        else:
            raise ValueError(f"Unsupported file type: {path.suffix}")
        
        return loader.load()
    
    def ingest_directory(
        self,
        directory: str,
        file_patterns: list[str] = ["*.txt", "*.pdf", "*.md"]
    ) -> dict:
        """Ingest all matching files from directory"""
        
        path = Path(directory)
        all_files = []
        
        # Collect all matching files
        for pattern in file_patterns:
            all_files.extend(path.rglob(pattern))
        
        print(f"Found {len(all_files)} files to ingest")
        
        total_chunks = 0
        results = {"successful": [], "failed": []}
        
        # Process each file
        for file_path in tqdm(all_files, desc="Ingesting documents"):
            try:
                # Load document
                documents = self.load_document(str(file_path))
                
                # Add metadata
                for doc in documents:
                    doc.metadata["source"] = str(file_path)
                    doc.metadata["filename"] = file_path.name
                
                # Split into chunks
                chunks = self.text_splitter.split_documents(documents)
                
                # Add to vector store
                self.vectorstore.add_documents(chunks)
                
                total_chunks += len(chunks)
                results["successful"].append({
                    "file": str(file_path),
                    "chunks": len(chunks)
                })
                
            except Exception as e:
                print(f"Failed to ingest {file_path}: {e}")
                results["failed"].append({
                    "file": str(file_path),
                    "error": str(e)
                })
        
        print(f"\nIngestion complete: {total_chunks} total chunks")
        print(f"Successful: {len(results['successful'])} files")
        print(f"Failed: {len(results['failed'])} files")
        
        return results
    
    def ingest_single_file(self, file_path: str) -> int:
        """Ingest single file"""
        documents = self.load_document(file_path)
        
        # Add metadata
        for doc in documents:
            doc.metadata["source"] = file_path
        
        chunks = self.text_splitter.split_documents(documents)
        self.vectorstore.add_documents(chunks)
        
        return len(chunks)

# Usage
if __name__ == "__main__":
    from knowledge.vectorstore import VectorStoreManager
    
    # Initialize vector store
    manager = VectorStoreManager()
    
    # Create pipeline
    pipeline = DocumentIngestionPipeline(manager.vectorstore)
    
    # Ingest directory
    results = pipeline.ingest_directory("./documents")
    
    print(f"Ingestion results: {results}")
```

---

## Success Criteria

✅ All document types load correctly  
✅ Chunking strategy preserves context  
✅ Metadata captured properly  
✅ Progress tracking works  
✅ Error handling prevents pipeline failure

---

## Integration

**Requires:** Vector store from Knowledge Engineering Agent  
**Provides:** Populated knowledge base ready for RAG
