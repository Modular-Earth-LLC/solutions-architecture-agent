# Add Sidebar Configuration Controls

**Agent:** Streamlit UI Development Agent  
**Category:** UI Development  
**Complexity:** Simple  
**Duration:** 30-60 minutes

---

## Purpose

Add comprehensive sidebar configuration controls for Claude model selection, parameters, and application settings.

---

## Instructions

Create sidebar with:

1. **Model selection dropdown**
2. **Parameter controls** (temperature, max_tokens)
3. **System prompt editor**
4. **Save/reset configuration**
5. **Session state persistence**

---

## Expected Output

```python
import streamlit as st

# Initialize config in session state
if "config" not in st.session_state:
    st.session_state.config = {
        "model": "claude-3-5-sonnet-20241022",
        "temperature": 1.0,
        "max_tokens": 4096,
        "system_prompt": "You are a helpful AI assistant."
    }

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Model selection
    model = st.selectbox(
        "Claude Model",
        options=[
            "claude-3-5-sonnet-20241022",
            "claude-3-5-haiku-20241022",
            "claude-3-opus-20240229"
        ],
        index=0,
        help="Select Claude model - Sonnet (balanced), Haiku (fast), Opus (best)"
    )
    
    # Temperature
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=st.session_state.config["temperature"],
        step=0.1,
        help="Higher = more creative, Lower = more focused"
    )
    
    # Max tokens
    max_tokens = st.number_input(
        "Max Tokens",
        min_value=256,
        max_value=8192,
        value=st.session_state.config["max_tokens"],
        step=256,
        help="Maximum response length"
    )
    
    # System prompt
    st.subheader("System Prompt")
    system_prompt = st.text_area(
        "Instructions for Claude",
        value=st.session_state.config["system_prompt"],
        height=150,
        help="Define Claude's behavior and capabilities"
    )
    
    st.divider()
    
    # Action buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("💾 Save", use_container_width=True):
            st.session_state.config = {
                "model": model,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "system_prompt": system_prompt
            }
            st.success("✅ Saved!")
    
    with col2:
        if st.button("🔄 Reset", use_container_width=True):
            st.session_state.config = {
                "model": "claude-3-5-sonnet-20241022",
                "temperature": 1.0,
                "max_tokens": 4096,
                "system_prompt": "You are a helpful AI assistant."
            }
            st.rerun()
    
    # Display current settings
    st.divider()
    st.caption("**Current Settings:**")
    st.caption(f"Model: {st.session_state.config['model'].split('-')[2]}")
    st.caption(f"Temp: {st.session_state.config['temperature']}")
    st.caption(f"Max Tokens: {st.session_state.config['max_tokens']}")
```

---

## Success Criteria

✅ Sidebar displays all controls  
✅ Configuration saves to session state  
✅ Reset restores defaults  
✅ Settings apply to Claude calls  
✅ UI is intuitive and organized

---

## Integration

Configuration will be used by Claude Integration Agent for API calls.
