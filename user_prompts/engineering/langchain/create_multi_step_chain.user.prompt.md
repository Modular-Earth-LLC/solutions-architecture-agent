# Create Multi-Step LangChain Chain

**Agent:** LangChain Orchestration Agent  
**Category:** LLM Orchestration  
**Complexity:** Intermediate  
**Duration:** 1-2 hours

---

## Purpose

Build multi-step processing chain using LangChain Expression Language (LCEL) for complex workflows like summarize-then-translate or analyze-then-recommend.

---

## Instructions

Create multi-step chain with:

1. **Step 1:** Initial processing (e.g., summarization)
2. **Step 2:** Secondary processing (e.g., translation)
3. **LCEL pipe composition**
4. **Intermediate result passing**
5. **Error handling**

---

## Expected Output

```python
# src/workflows/multi_step.py

from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os

def create_summarize_translate_chain():
    """
    Multi-step chain: Summarize text, then translate
    
    Input: {"text": str, "language": str}
    Output: Translated summary
    """
    
    # Initialize Claude
    chat = ChatAnthropic(
        model="claude-3-5-sonnet-20241022",
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    
    # Step 1: Summarize
    summarize_prompt = ChatPromptTemplate.from_template(
        "Summarize the following text in 2-3 sentences:\n\n{text}"
    )
    
    # Step 2: Translate
    translate_prompt = ChatPromptTemplate.from_template(
        "Translate the following text to {language}:\n\n{summary}"
    )
    
    # Build multi-step chain with LCEL
    chain = (
        # Pass through text
        {"text": lambda x: x["text"]}
        | summarize_prompt
        | chat
        | StrOutputParser()
        # Transform: add language to summary
        | (lambda summary: {
            "summary": summary,
            "language": "Spanish"  # Or from input
        })
        | translate_prompt
        | chat
        | StrOutputParser()
    )
    
    return chain

def create_analyze_recommend_chain():
    """
    Multi-step chain: Analyze data, then recommend actions
    
    Input: {"data": str, "context": str}
    Output: Recommendations based on analysis
    """
    
    chat = ChatAnthropic(model="claude-3-5-sonnet-20241022")
    
    # Step 1: Analyze
    analyze_prompt = ChatPromptTemplate.from_template(
        """Analyze the following data:

{data}

Context: {context}

Provide a structured analysis with key insights."""
    )
    
    # Step 2: Recommend
    recommend_prompt = ChatPromptTemplate.from_template(
        """Based on this analysis:

{analysis}

Provide 3-5 specific, actionable recommendations."""
    )
    
    # Build chain
    chain = (
        {"data": lambda x: x["data"], "context": lambda x: x["context"]}
        | analyze_prompt
        | chat
        | StrOutputParser()
        | (lambda analysis: {"analysis": analysis})
        | recommend_prompt
        | chat
        | StrOutputParser()
    )
    
    return chain

# Usage
if __name__ == "__main__":
    chain = create_summarize_translate_chain()
    
    result = chain.invoke({
        "text": "Long English text here...",
        "language": "French"
    })
    
    print(result)
```

---

## Success Criteria

✅ Multi-step chain executes correctly  
✅ Intermediate results pass properly  
✅ LCEL composition clear and maintainable  
✅ Error handling works  
✅ Chain is reusable

---

## Best Practices

- Use lambda functions for data transformation between steps
- Keep each step focused on single task
- Use descriptive variable names in dictionaries
- Test each step independently first
- Handle errors at each step
