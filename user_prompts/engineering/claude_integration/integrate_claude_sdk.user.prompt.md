# Integrate Anthropic Claude SDK

**Agent:** Anthropic Claude Integration Agent  
**Category:** LLM Integration  
**Complexity:** Intermediate  
**Duration:** 1-2 hours

---

## Purpose

Implement Anthropic Claude SDK integration with error handling, retry logic, and usage tracking for Python applications.

---

## Instructions

Create Claude SDK integration module with:

1. **Client initialization** (from environment variables)
2. **Synchronous message API**
3. **Error handling and retry logic**
4. **Usage tracking**
5. **Rate limiting**
6. **Response parsing**

---

## Expected Output

```python
# src/claude/client.py

from anthropic import Anthropic, APIError, RateLimitError
from typing import List, Dict, Optional
import os
import time

class ClaudeService:
    """Production-ready Claude API integration"""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-3-5-sonnet-20241022",
        max_tokens: int = 4096,
        temperature: float = 1.0
    ):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY required")
        
        self.client = Anthropic(api_key=self.api_key)
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.usage_history = []
    
    def send_message(
        self,
        messages: List[Dict],
        system_prompt: str = "",
        max_retries: int = 3
    ) -> Dict:
        """Send message to Claude with retry logic"""
        
        for attempt in range(max_retries):
            try:
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=self.max_tokens,
                    temperature=self.temperature,
                    system=system_prompt,
                    messages=messages
                )
                
                # Track usage
                self._track_usage(response)
                
                return self._parse_response(response)
            
            except RateLimitError:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt
                    time.sleep(wait_time)
                else:
                    raise
            
            except APIError as e:
                raise Exception(f"Claude API error: {str(e)}")
        
        raise Exception("Max retries exceeded")
    
    def _parse_response(self, response) -> Dict:
        """Parse API response"""
        return {
            "text": response.content[0].text,
            "model": response.model,
            "usage": {
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
                "total_tokens": response.usage.input_tokens + response.usage.output_tokens
            },
            "stop_reason": response.stop_reason
        }
    
    def _track_usage(self, response):
        """Track token usage for monitoring"""
        self.usage_history.append({
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "model": self.model
        })
    
    def get_total_tokens(self) -> int:
        """Get total tokens used"""
        return sum(
            h["input_tokens"] + h["output_tokens"]
            for h in self.usage_history
        )

# Usage example
if __name__ == "__main__":
    service = ClaudeService()
    
    response = service.send_message(
        messages=[{"role": "user", "content": "Hello Claude"}],
        system_prompt="You are a helpful assistant."
    )
    
    print(response["text"])
    print(f"Tokens used: {response['usage']['total_tokens']}")
```

---

## Success Criteria

✅ Claude SDK properly initialized  
✅ Error handling prevents crashes  
✅ Retry logic works for rate limits  
✅ Usage tracking accurate  
✅ Responses parsed correctly

---

## Testing

Create tests for:
- Successful API calls
- Rate limit handling
- Error recovery
- Usage tracking accuracy
