# Create Pytest Test Suite

**Agent:** Testing & QA Agent  
**Category:** Quality Assurance  
**Complexity:** Intermediate  
**Duration:** 2-3 hours

---

## Purpose

Create comprehensive pytest test suite for Python AI application covering unit tests, integration tests, and data quality tests.

---

## Instructions

Create test suite with:

1. **Test configuration** (pytest.ini, conftest.py)
2. **Unit tests** for core components
3. **Integration tests** for workflows
4. **Mocking** for external APIs
5. **Coverage reporting**

---

## Expected Output

```python
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --verbose
    --cov=src
    --cov-report=html
    --cov-report=term
markers =
    unit: Unit tests
    integration: Integration tests
    slow: Slow-running tests

# conftest.py
import pytest
from unittest.mock import Mock
import os

@pytest.fixture
def mock_claude_client():
    """Mock Anthropic client for testing"""
    client = Mock()
    mock_response = Mock()
    mock_response.content = [Mock(text="Test response")]
    mock_response.usage.input_tokens = 10
    mock_response.usage.output_tokens = 5
    client.messages.create.return_value = mock_response
    return client

@pytest.fixture
def test_env():
    """Set up test environment variables"""
    os.environ['ANTHROPIC_API_KEY'] = 'test-key'
    yield
    del os.environ['ANTHROPIC_API_KEY']

# tests/test_claude_client.py
import pytest
from src.claude.client import ClaudeService

@pytest.mark.unit
def test_client_initialization(test_env):
    """Test Claude client initializes correctly"""
    service = ClaudeService()
    assert service.model == "claude-3-5-sonnet-20241022"
    assert service.max_tokens == 4096

@pytest.mark.unit
def test_send_message(mock_claude_client):
    """Test sending message to Claude"""
    service = ClaudeService()
    service.client = mock_claude_client
    
    result = service.send_message([
        {"role": "user", "content": "Hello"}
    ])
    
    assert result["text"] == "Test response"
    assert result["usage"]["input_tokens"] == 10

@pytest.mark.integration
def test_end_to_end_conversation():
    """Test complete conversation flow"""
    # Requires actual API key for integration tests
    # Skip if key not available
    if not os.getenv("ANTHROPIC_API_KEY"):
        pytest.skip("API key not available")
    
    service = ClaudeService()
    response = service.send_message([
        {"role": "user", "content": "What is 2+2?"}
    ])
    
    assert "4" in response["text"]

# Run tests
# pytest tests/ --cov=src --cov-report=html
```

---

## Success Criteria

✅ Pytest configuration complete  
✅ Unit tests cover core logic  
✅ Integration tests validate flows  
✅ Mocking works correctly  
✅ >80% code coverage achieved

---

## Testing Commands

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific markers
pytest -m unit
pytest -m integration

# Run specific test file
pytest tests/test_claude_client.py
```
