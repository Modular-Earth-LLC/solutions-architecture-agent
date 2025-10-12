# Validate RAG System Quality

**Agent:** Testing & QA Agent  
**Category:** Quality Assurance  
**Complexity:** Advanced  
**Duration:** 2-3 hours

---

## Purpose

Test RAG (Retrieval-Augmented Generation) system for retrieval accuracy, answer quality, and source citation correctness.

---

## Instructions

Create RAG validation suite with:

1. **Retrieval quality tests** (relevant documents returned)
2. **Answer accuracy tests** (Claude answers correctly from context)
3. **Citation accuracy** (sources cited correctly)
4. **Edge case handling** (no relevant docs, ambiguous queries)
5. **Performance benchmarks** (retrieval speed, answer latency)

---

## Expected Output

```python
# tests/test_rag_quality.py

import pytest
from src.knowledge.vectorstore import VectorStoreManager
from src.workflows.rag_chain import create_rag_chain

class TestRAGQuality:
    """Test RAG system quality and accuracy"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup RAG system for testing"""
        self.manager = VectorStoreManager()
        self.chain = create_rag_chain(self.manager.get_retriever())
        
        # Test data
        self.test_cases = [
            {
                "question": "What is the return policy?",
                "expected_keywords": ["return", "policy", "days"],
                "expected_source": "policy.txt"
            },
            {
                "question": "How do I contact support?",
                "expected_keywords": ["support", "contact", "email"],
                "expected_source": "support.txt"
            }
        ]
    
    def test_retrieval_relevance(self):
        """Test that retrieved documents are relevant"""
        retriever = self.manager.get_retriever()
        
        for test_case in self.test_cases:
            docs = retriever.get_relevant_documents(test_case["question"])
            
            # Should retrieve at least 1 document
            assert len(docs) > 0, f"No documents retrieved for: {test_case['question']}"
            
            # Top document should contain expected keywords
            top_doc = docs[0].page_content.lower()
            for keyword in test_case["expected_keywords"]:
                assert keyword in top_doc, f"Keyword '{keyword}' not in top result"
    
    def test_answer_accuracy(self):
        """Test that RAG chain answers correctly"""
        
        for test_case in self.test_cases:
            result = self.chain.invoke({
                "question": test_case["question"]
            })
            
            # Answer should contain expected keywords
            answer = result.lower()
            for keyword in test_case["expected_keywords"]:
                assert keyword in answer, \
                    f"Expected keyword '{keyword}' not in answer for: {test_case['question']}"
    
    def test_source_citations(self):
        """Test that sources are cited correctly"""
        
        for test_case in self.test_cases:
            result = self.chain.invoke({
                "question": test_case["question"]
            })
            
            # Should contain citation markers [1], [2], etc.
            assert "[1]" in result or "source:" in result.lower(), \
                "No source citation found in answer"
    
    def test_no_relevant_docs(self):
        """Test handling when no relevant documents exist"""
        
        result = self.chain.invoke({
            "question": "What is quantum mechanics?"  # Not in knowledge base
        })
        
        # Should indicate no relevant information found
        assert any(phrase in result.lower() for phrase in [
            "don't have information",
            "not found",
            "no relevant",
            "cannot answer"
        ])
    
    def test_retrieval_performance(self):
        """Test retrieval speed"""
        import time
        
        retriever = self.manager.get_retriever()
        
        times = []
        for _ in range(10):
            start = time.time()
            retriever.get_relevant_documents("test query")
            times.append(time.time() - start)
        
        avg_time = sum(times) / len(times)
        assert avg_time < 1.0, f"Retrieval too slow: {avg_time:.2f}s average"
    
    def test_answer_quality_metrics(self):
        """Test answer quality with metrics"""
        
        results = []
        for test_case in self.test_cases:
            answer = self.chain.invoke({"question": test_case["question"]})
            
            # Calculate quality metrics
            relevance_score = self._calculate_relevance(
                answer,
                test_case["expected_keywords"]
            )
            
            results.append({
                "question": test_case["question"],
                "relevance_score": relevance_score,
                "answer_length": len(answer)
            })
        
        # All should have good relevance
        for result in results:
            assert result["relevance_score"] >= 0.7, \
                f"Low relevance score: {result['relevance_score']}"
    
    def _calculate_relevance(self, answer: str, keywords: list[str]) -> float:
        """Calculate answer relevance score"""
        answer_lower = answer.lower()
        matches = sum(1 for kw in keywords if kw in answer_lower)
        return matches / len(keywords)

# Run tests
# pytest tests/test_rag_quality.py -v
```

---

## Success Criteria

✅ Retrieval returns relevant documents  
✅ Answers accurate based on context  
✅ Citations correct  
✅ Edge cases handled  
✅ Performance acceptable

---

## Quality Metrics

- Retrieval accuracy: >90%
- Answer relevance: >80%
- Citation accuracy: 100%
- Retrieval speed: <1s
- Answer latency: <5s
