import sqlite3
import os


#datafonder
os.makedirs("data", exist_ok=True)


_conn = sqlite3.connect("data/expenses.db", check_same_thread=False)  
_cursor = _conn.cursor()


allowed_categories_sql = (
        "'Bill Sharing', 'Family Expenses', 'Groceries', 'Lend/Borrow', 'Personal Use', 'Ride Sharing'"
    )
check_clause = f"CHECK (category IN ({allowed_categories_sql}))"

def init_db():
    _cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT {check_clause},
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    print("Main Table created")
    
 
    _conn.commit()

def get_conn():
    return _conn

def get_cursor():
    return _cursor

def reset_schema():
    _cursor.execute("DROP TABLE IF EXISTS expenses")
    _cursor.execute("DROP TABLE IF EXISTS budgets")
    init_db()
    print("Schema reset ✅")

