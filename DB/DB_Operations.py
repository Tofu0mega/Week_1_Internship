from .dbconfig import get_conn, get_cursor

cursor=get_cursor()
connection=get_conn()
def Add_Transaction(Transaction):
    try:
        name = Transaction["name"]
        amount = Transaction["amount"]
        category = Transaction["category"]
        insertionquery=cursor.execute("INSERT INTO expenses (name,amount,category) VALUES (?,?,?);",(name,amount,category))
        connection.commit()
    except Exception as e:
        print(e)
        input("Press Enter to continue...")
 
        

def getalltransaction():
    try:
        transactiontable=cursor.execute("SELECT * FROM expenses")
        transaction_data=transactiontable.fetchall()
        return transaction_data
    except Exception as e:
        print(e)
        input("Press Enter to continue...")


def getdefinedbudget():
    try:
        budgettable=cursor.execute("SELECT * FROM budgets")
        budget_data=budgettable.fetchall()
        return budget_data
    except Exception as e:
        print(e)
        input("Press Enter to continue...")


def definebudget(Transaction):
    try:
        category = Transaction["category"]
        amount = Transaction["amount"]
        cursor.execute(f'''
        INSERT INTO budgets (category, budget)
        VALUES (?, ?)
        ON CONFLICT(category) DO UPDATE SET
            budget = excluded.budget,
            timestamp = CURRENT_TIMESTAMP
        ''', (category, amount))
        connection.commit()
    except Exception as e:
        print(e)
        input("Press Enter to continue...")

    
def getamount_by_category():
    try:
        query = '''
        SELECT 
            e.category,
            SUM(e.amount) AS total_amount,
            b.budget AS "limit"
        FROM expenses e
        LEFT JOIN budgets b ON e.category = b.category
        GROUP BY e.category
        '''
        amountbycata = cursor.execute(query)
        categorical_data = amountbycata.fetchall()
        return categorical_data
    except Exception as e:
        print(e)
        input("Press Enter to continue...")
