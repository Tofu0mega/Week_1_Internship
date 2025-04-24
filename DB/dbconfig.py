import sqlite3
import os
# import json


os.makedirs("data", exist_ok=True)




default_categories =  [
        "Food",
        "Entertainment",
        "Transportation",
        "Education",
        "Michalleneous",
        "Rent"
    ]





_conn = sqlite3.connect("data/expenses.db", check_same_thread=False)
_cursor = _conn.cursor()

def init_db():
    
    _cursor.execute('PRAGMA foreign_keys = ON')
    _cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT UNIQUE,
            budget REAL 
            
        )
    ''')
    
    _cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category) REFERENCES budgets(category) ON DELETE CASCADE
        )
    ''')
    _conn.commit()
    result=_cursor.execute("SELECT * FROM budgets")
    data=result.fetchall()
   
    if not data: 
        _cursor.executemany(
            "INSERT OR IGNORE INTO budgets (category,budget) VALUES (?,3000)",
        [(cat,) for cat in default_categories]
        

 
        )
        _conn.commit()


    
    

    print("📦 Tables created/verified")

def get_conn():
    return _conn

def get_cursor():
    return _cursor

def reset_schema():
    _cursor.execute("DROP TABLE IF EXISTS expenses")
    _cursor.execute("DROP TABLE IF EXISTS budgets")
    
    print("♻️ Schema reset")

