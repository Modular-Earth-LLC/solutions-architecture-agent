# Create Multi-Page Streamlit Application

**Agent:** Streamlit UI Development Agent  
**Category:** UI Development  
**Complexity:** Intermediate  
**Duration:** 1-2 hours

---

## Purpose

Structure a Streamlit application with multiple pages for complex AI systems with different functionalities (chat, documents, analytics, settings).

---

## Instructions

Create multi-page Streamlit app with:

1. **Main App** (`streamlit_app.py`) - Landing page or default view
2. **Pages Directory** (`pages/`) - Individual page files
3. **Shared Components** - Reusable UI elements
4. **Navigation** - Automatic sidebar navigation

---

## Expected Structure

```
outputs/prototypes/[project]/
├── streamlit_app.py           # Main app (Chat page)
├── pages/
│   ├── 1_💬_Chat.py           # Chat interface
│   ├── 2_📄_Documents.py      # Document analysis
│   ├── 3_📊_Analytics.py      # Analytics dashboard
│   └── 4_⚙️_Settings.py       # Configuration
└── components/
    ├── __init__.py
    └── shared.py              # Shared components
```

---

## Expected Output

```python
# streamlit_app.py (main)
import streamlit as st

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Assistant")
st.write("Welcome! Use the sidebar to navigate.")

# pages/1_💬_Chat.py
import streamlit as st

st.set_page_config(page_title="Chat", page_icon="💬")
st.title("💬 Chat with Claude")
# Chat interface here

# pages/2_📄_Documents.py
import streamlit as st

st.set_page_config(page_title="Documents", page_icon="📄")
st.title("📄 Document Analysis")
# Document upload and analysis here

# pages/3_📊_Analytics.py
import streamlit as st

st.set_page_config(page_title="Analytics", page_icon="📊")
st.title("📊 Usage Analytics")
# Analytics dashboard here

# pages/4_⚙️_Settings.py
import streamlit as st

st.set_page_config(page_title="Settings", page_icon="⚙️")
st.title("⚙️ Settings")
# Configuration options here
```

---

## Success Criteria

✅ Multi-page structure works correctly  
✅ Navigation in sidebar functional  
✅ Page icons and titles display properly  
✅ Shared state accessible across pages

---

## Best Practices

- Use emojis in page names for visual navigation
- Prefix with numbers for ordering (1_, 2_, 3_)
- Keep pages focused on single functionality
- Share state via st.session_state
