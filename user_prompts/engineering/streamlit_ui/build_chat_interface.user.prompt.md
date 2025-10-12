# Build Streamlit Chat Interface

**Agent:** Streamlit UI Development Agent  
**Category:** UI Development  
**Complexity:** Intermediate  
**Duration:** 1-2 hours

---

## Purpose

Build a production-quality Streamlit chat interface with session state management, message history display, and integration points for Claude API calls.

---

## Instructions for Agent

Create a complete Streamlit chat interface with the following features:

### Requirements

1. **Chat Display**
   - Display message history using `st.chat_message`
   - Show user and assistant messages with proper formatting
   - Support markdown rendering in messages
   - Display timestamps

2. **User Input**
   - Use `st.chat_input` for message entry
   - Handle empty input gracefully
   - Show placeholder text
   - Clear input after submission

3. **Session State Management**
   - Initialize `messages` list in session state
   - Persist conversation across reruns
   - Support conversation clearing
   - Track conversation metadata

4. **Integration Points**
   - Provide clear integration point for Claude Integration Agent
   - Pass messages to backend processing
   - Display streaming responses
   - Handle loading states

5. **UI Polish**
   - Add chat header with title
   - Include "Clear Chat" button
   - Show token usage (if available)
   - Responsive layout

---

## Expected Output

```python
# streamlit_app.py

import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="AI Chat",
    page_icon="💬",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.title("💬 Chat with Claude")
st.caption("Powered by Anthropic Claude")

# Sidebar with controls
with st.sidebar:
    st.header("Controls")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.info(f"Messages: {len(st.session_state.messages)}")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "timestamp" in msg:
            st.caption(msg["timestamp"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Add user message
    timestamp = datetime.now().strftime("%H:%M")
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
        "timestamp": timestamp
    })
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
        st.caption(timestamp)
    
    # Assistant response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        
        # INTEGRATION POINT: Claude Integration Agent handles this
        # For now, show loading state
        with st.spinner("Thinking..."):
            # Claude Integration Agent will:
            # 1. Take st.session_state.messages
            # 2. Call Claude API
            # 3. Return response
            # 4. Update st.session_state.messages
            pass
```

---

## Success Criteria

✅ Chat interface renders correctly  
✅ Messages display with proper formatting  
✅ Session state persists across reruns  
✅ Clear integration point for Claude agent  
✅ UI is clean and professional

---

## Integration Notes

**Collaborates With:**
- Claude Integration Agent (will implement the API call at integration point)

**Next Steps After This Prompt:**
- Use Claude Integration Agent to implement backend processing
- Add streaming response handling
- Implement error handling UI
