# Design SQLite Database Schema

**Agent:** Data Engineering Agent  
**Category:** Data Engineering  
**Complexity:** Intermediate  
**Duration:** 1-2 hours

---

## Purpose

Design and implement SQLite database schema for AI application data (users, conversations, messages, usage tracking).

---

## Instructions

Create database schema with:

1. **Entity design** (users, conversations, messages)
2. **Relationships** (foreign keys)
3. **Indexes** (for query performance)
4. **Constraints** (data validation)
5. **Migration script**

---

## Expected Output

```python
# src/database/schema.py

import sqlite3
from contextlib import contextmanager

@contextmanager
def get_connection(db_path: str = "app.db"):
    """Database connection context manager"""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def create_schema(db_path: str = "app.db"):
    """Create database schema"""
    with get_connection(db_path) as conn:
        conn.executescript("""
        -- Users table
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        -- Conversations table
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT,
            model TEXT DEFAULT 'claude-3-5-sonnet-20241022',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );
        
        -- Messages table
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id INTEGER NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('user', 'assistant', 'system')),
            content TEXT NOT NULL,
            tokens_input INTEGER,
            tokens_output INTEGER,
            cost REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (conversation_id) REFERENCES conversations (id) ON DELETE CASCADE
        );
        
        -- Usage analytics table
        CREATE TABLE IF NOT EXISTS usage_analytics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            date DATE NOT NULL,
            total_messages INTEGER DEFAULT 0,
            total_tokens INTEGER DEFAULT 0,
            total_cost REAL DEFAULT 0.0,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );
        
        -- Indexes for performance
        CREATE INDEX IF NOT EXISTS idx_messages_conversation 
        ON messages(conversation_id);
        
        CREATE INDEX IF NOT EXISTS idx_messages_created 
        ON messages(created_at DESC);
        
        CREATE INDEX IF NOT EXISTS idx_conversations_user 
        ON conversations(user_id);
        
        CREATE INDEX IF NOT EXISTS idx_conversations_updated 
        ON conversations(updated_at DESC);
        
        CREATE INDEX IF NOT EXISTS idx_analytics_user_date 
        ON usage_analytics(user_id, date);
        """)
    print("Schema created successfully")

# Usage
if __name__ == "__main__":
    create_schema()
```

---

## Success Criteria

✅ Schema supports all application needs  
✅ Relationships properly defined  
✅ Indexes optimize common queries  
✅ Constraints prevent invalid data  
✅ Schema is migration-ready

---

## Best Practices

- Use foreign keys with CASCADE
- Index all foreign keys
- Add timestamps for auditing
- Use CHECK constraints for validation
- Keep schema normalized
