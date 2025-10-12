# Implement Streaming Claude Responses

**Agent:** Anthropic Claude Integration Agent  
**Category:** LLM Integration  
**Complexity:** Advanced  
**Duration:** 2-3 hours

---

## Purpose

Implement streaming responses from Claude API for real-time user feedback in Streamlit applications.

---

## Instructions

Implement streaming with:

1. **Claude streaming API**
2. **Streamlit integration** (real-time display)
3. **Event handling** (text chunks, completion)
4. **Error handling during streams**
5. **Usage tracking for streamed responses**

---

## Expected Output

```python
# src/claude/streaming.py

from anthropic import Anthropic
import streamlit as st

def stream_claude_response(
    client: Anthropic,
    messages: list[dict],
    system_prompt: str = "",
    model: str = "claude-3-5-sonnet-20241022",
    max_tokens: int = 4096
):
    """
    Stream response from Claude with Streamlit integration
    
    Yields text chunks as they arrive and displays in Streamlit
    """
    full_text = ""
    
    with client.messages.stream(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=messages
    ) as stream:
        # Stream text chunks
        for text in stream.text_stream:
            full_text += text
            yield text
        
        # Get final message with usage stats
        final_message = stream.get_final_message()
        
        # Return usage info
        yield {
            "usage": {
                "input_tokens": final_message.usage.input_tokens,
                "output_tokens": final_message.usage.output_tokens
            }
        }

# Usage in Streamlit
def display_streaming_response(client, messages, system_prompt=""):
    """Display streaming response in Streamlit"""
    
    response_placeholder = st.empty()
    full_response = ""
    
    for chunk in stream_claude_response(client, messages, system_prompt):
        if isinstance(chunk, str):
            full_response += chunk
            response_placeholder.markdown(full_response + "▌")  # Cursor effect
        else:
            # Final chunk with usage
            response_placeholder.markdown(full_response)
            st.caption(f"Tokens: {chunk['usage']['input_tokens']} in, {chunk['usage']['output_tokens']} out")
    
    return full_response

# Complete example
if prompt := st.chat_input("Message"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        response = display_streaming_response(
            client,
            st.session_state.messages,
            system_prompt="You are a helpful assistant."
        )
        st.session_state.messages.append({"role": "assistant", "content": response})
```

---

## Success Criteria

✅ Streaming displays in real-time  
✅ Cursor effect during streaming  
✅ Usage stats shown after completion  
✅ Error handling during stream  
✅ Full response captured correctly

---

## Integration

**Collaborates With:**
- Streamlit UI Agent (displays streaming UI)
