# Build RAG Chain with LangChain

**Agent:** LangChain Orchestration Agent  
**Category:** LLM Orchestration  
**Complexity:** Advanced  
**Duration:** 2-3 hours

---

## Purpose

Build Retrieval-Augmented Generation (RAG) chain using LangChain with Claude for question-answering over documents.

---

## Instructions

Implement RAG chain with:

1. **Retriever integration** (from Knowledge Engineering Agent)
2. **RAG prompt template**
3. **LCEL chain composition**
4. **Source citation**
5. **Relevance filtering**

---

## Expected Output

```python
# src/workflows/rag_chain.py

from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.documents import Document
import os

def create_rag_chain(retriever):
    """
    Create RAG chain for question answering
    
    Args:
        retriever: Vector store retriever from Knowledge Engineering Agent
    
    Returns:
        Runnable RAG chain
    """
    
    # Initialize Claude
    chat = ChatAnthropic(
        model="claude-3-5-sonnet-20241022",
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        max_tokens=4096
    )
    
    # Format documents with citations
    def format_docs(docs: list[Document]) -> str:
        formatted = []
        for i, doc in enumerate(docs, 1):
            content = doc.page_content
            source = doc.metadata.get('source', 'Unknown')
            formatted.append(f"[{i}] {content}\nSource: {source}")
        return "\n\n".join(formatted)
    
    # RAG prompt
    rag_prompt = ChatPromptTemplate.from_template("""
Answer the question based ONLY on the following context. Include source citations [1], [2], etc.

Context:
{context}

Question: {question}

Answer with citations:""")
    
    # Build RAG chain with LCEL
    rag_chain = (
        RunnableParallel({
            "context": lambda x: format_docs(retriever.get_relevant_documents(x["question"])),
            "question": RunnablePassthrough()
        })
        | rag_prompt
        | chat
        | StrOutputParser()
    )
    
    return rag_chain

# Usage
if __name__ == "__main__":
    # Assume retriever from Knowledge Engineering Agent
    # retriever = setup_retriever()
    
    chain = create_rag_chain(retriever)
    
    result = chain.invoke({
        "question": "What is the return policy?"
    })
    
    print(result)
```

---

## Success Criteria

✅ RAG chain retrieves relevant documents  
✅ Claude answers based on context  
✅ Source citations included  
✅ Relevance filtering works  
✅ Chain is reusable and testable

---

## Integration

**Requires:** Knowledge Engineering Agent (provides retriever)  
**Collaborates With:** Claude Integration Agent
