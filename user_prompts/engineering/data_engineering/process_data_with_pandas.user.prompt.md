# Process Data with pandas

**Agent:** Data Engineering Agent  
**Category:** Data Engineering  
**Complexity:** Intermediate  
**Duration:** 1-2 hours

---

## Purpose

Implement data processing and analysis using pandas for AI application analytics, usage tracking, and reporting.

---

## Instructions

Create data processing module with:

1. **Load data from SQLite**
2. **Data cleaning and transformation**
3. **Aggregation and analytics**
4. **Export to various formats**
5. **Visualization-ready outputs**

---

## Expected Output

```python
# src/data/analytics.py

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sqlite3

class UsageAnalytics:
    """Process and analyze AI application usage data"""
    
    def __init__(self, db_path: str = "app.db"):
        self.db_path = db_path
    
    def load_usage_data(
        self,
        start_date: str = None,
        end_date: str = None
    ) -> pd.DataFrame:
        """Load usage data from database"""
        
        query = """
        SELECT 
            u.username,
            c.id as conversation_id,
            c.title as conversation_title,
            m.role,
            m.tokens_input,
            m.tokens_output,
            m.cost,
            DATE(m.created_at) as date,
            m.created_at as timestamp
        FROM messages m
        JOIN conversations c ON m.conversation_id = c.id
        JOIN users u ON c.user_id = u.id
        WHERE 1=1
        """
        
        params = []
        if start_date:
            query += " AND DATE(m.created_at) >= ?"
            params.append(start_date)
        if end_date:
            query += " AND DATE(m.created_at) <= ?"
            params.append(end_date)
        
        query += " ORDER BY m.created_at DESC"
        
        with sqlite3.connect(self.db_path) as conn:
            df = pd.read_sql_query(query, conn, params=params)
        
        # Data type conversions
        df['date'] = pd.to_datetime(df['date'])
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['total_tokens'] = df['tokens_input'] + df['tokens_output']
        
        return df
    
    def daily_summary(self, df: pd.DataFrame) -> pd.DataFrame:
        """Generate daily usage summary"""
        
        summary = df.groupby(['username', 'date']).agg({
            'conversation_id': 'nunique',  # Unique conversations
            'role': 'count',  # Total messages
            'total_tokens': 'sum',
            'cost': 'sum'
        }).rename(columns={
            'conversation_id': 'conversations',
            'role': 'messages',
            'total_tokens': 'tokens',
            'cost': 'total_cost'
        }).reset_index()
        
        # Calculate averages
        summary['avg_tokens_per_message'] = summary['tokens'] / summary['messages']
        summary['avg_cost_per_conversation'] = summary['total_cost'] / summary['conversations']
        
        return summary
    
    def user_statistics(self, df: pd.DataFrame) -> pd.DataFrame:
        """Generate per-user statistics"""
        
        stats = df.groupby('username').agg({
            'conversation_id': 'nunique',
            'role': 'count',
            'total_tokens': 'sum',
            'cost': 'sum',
            'date': ['min', 'max']
        }).reset_index()
        
        # Flatten column names
        stats.columns = [
            'username', 'conversations', 'messages',
            'total_tokens', 'total_cost', 'first_use', 'last_use'
        ]
        
        # Calculate days active
        stats['days_active'] = (
            pd.to_datetime(stats['last_use']) - pd.to_datetime(stats['first_use'])
        ).dt.days + 1
        
        stats['avg_messages_per_day'] = stats['messages'] / stats['days_active']
        
        return stats.sort_values('total_tokens', ascending=False)
    
    def export_reports(self, output_dir: str = "./reports"):
        """Generate and export all reports"""
        
        # Load data (last 30 days)
        start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        df = self.load_usage_data(start_date=start_date)
        
        # Generate reports
        daily = self.daily_summary(df)
        users = self.user_statistics(df)
        
        # Export to CSV
        daily.to_csv(f"{output_dir}/daily_usage.csv", index=False)
        users.to_csv(f"{output_dir}/user_statistics.csv", index=False)
        
        # Export to Excel (multiple sheets)
        with pd.ExcelWriter(f"{output_dir}/usage_report.xlsx") as writer:
            daily.to_excel(writer, sheet_name='Daily Usage', index=False)
            users.to_excel(writer, sheet_name='User Stats', index=False)
            df.to_excel(writer, sheet_name='Raw Data', index=False)
        
        return {
            "daily_report": f"{output_dir}/daily_usage.csv",
            "user_report": f"{output_dir}/user_statistics.csv",
            "excel_report": f"{output_dir}/usage_report.xlsx"
        }

# Usage
if __name__ == "__main__":
    analytics = UsageAnalytics()
    
    # Generate reports
    reports = analytics.export_reports()
    print(f"Reports generated: {reports}")
    
    # Display summary
    df = analytics.load_usage_data()
    daily = analytics.daily_summary(df)
    print(daily.head())
```

---

## Success Criteria

✅ Data loads correctly from SQLite  
✅ Transformations produce correct results  
✅ Aggregations calculate accurately  
✅ Reports export in multiple formats  
✅ Performance is acceptable

---

## Integration

**Uses Data From:** Data Engineering Agent (SQLite schema)  
**Provides To:** Streamlit UI Agent (for dashboard display)
