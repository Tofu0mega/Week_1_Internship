from .dbconfig import get_conn, get_cursor
from datetime import datetime,timedelta
import pandas as pd
cursor=get_cursor()
connection=get_conn()

def get_month_start():
    today=datetime.today()
    start_of_month=today.replace(day=1)
    return start_of_month.strftime('%Y-%m-%d')


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
       

def getalltransactionmnth():
    try:
        startofmnth=get_month_start()
        transactiontable=cursor.execute("SELECT * FROM expenses WHERE date >=?",(startofmnth,))
        
        return transactiontable
    except Exception as e:
        print(e)
        input("Press Enter to continue...")
        
def getalltransaction():
    try:
      
        transactiontable=cursor.execute("SELECT * FROM expenses ")
        
        return transactiontable
    except Exception as e:
        print(e)
        input("Press Enter to continue...")


def getdefinedbudget():
    try:
      
        budgettable=cursor.execute("SELECT * FROM budgets")
        
        return budgettable
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
            budget = excluded.budget
            
        ''', (category, amount))
        connection.commit()
    except Exception as e:
        print(e)
        input("Press Enter to continue...")

    
def getamount_by_category():
    try:
        startofmnth=get_month_start()
        amountbycata = cursor.execute('''
                SELECT 
            e.category,
            SUM(e.amount) AS total_amount,
            b.budget,
            (b.budget - SUM(e.amount)) AS available_balance
        FROM expenses e
        LEFT JOIN budgets b ON e.category = b.category
        WHERE e.date >= ?
        GROUP BY e.category, b.budget

        
        
        ''',(startofmnth,))
       
        return amountbycata
    except Exception as e:
        print(e)
        input("Press Enter to continue...")


def get_status():
    try:
        startofmnth=get_month_start()
        status_table=cursor.execute("SELECT category,budget,(CASE WHEN budget >(SELECT SUM(amount) FROM expenses WHERE category= budgets.category AND date>=?) THEN 'Under_Budget' ELSE 'Over_Budget' END) AS status FROM budgets;",(startofmnth,))
        return status_table
    except Exception as e:
        print(e)
        input("Press Enter to continue")
        

def display_table(cursor,Status=False):
    if Status:
        rows =cursor.fetchall()
        columns= [desc[0] for desc in cursor.description]
        dataframe= pd.DataFrame(rows,columns=columns) 
        status_cursor=get_status()
        status_rows=status_cursor.fetchall()
        status_columns=[desc[0] for desc in status_cursor.description]
        status_dataframe=pd.DataFrame(status_rows,columns=status_columns)
        final_dataframe=pd.merge(dataframe,status_dataframe,on=["budget","category"],how="left")
        if(final_dataframe.empty):
            print("No Records To Show")
        else:
            print(final_dataframe.to_string(index=False))
    else:    
        rows =cursor.fetchall()
        columns= [desc[0] for desc in cursor.description]
        dataframe= pd.DataFrame(rows,columns=columns)    
        if(dataframe.empty):
            print("No Records to Show")
        else:
            print(dataframe.to_string(index=False))
            
            
def delete_record(id):
    try:
        result=cursor.execute("DELETE FROM expenses WHERE id = ?",(id,))
        if result.rowcount == 0:
            return 0;
        else :
            connection.commit()
            return 1;
    except Exception as e:
        print(e)
        input("Press Enter to Exit")



def edit_record(NewData):
    try:
        targetid=NewData["id"]
        newname=NewData["name"]
        newamount=NewData["amount"]
        newcategory=NewData["category"]
        result= cursor.execute("UPDATE expenses SET name=?,amount=?,category=? WHERE id=?",(newname,newamount,newcategory,targetid))
        if result.rowcount == 0:
            return 0;
        else :
            connection.commit()
            return 1;
    except Exception as e:
        print(e)
        input("Press Enter to Continue")



def check_record(id):
    try:
        result=cursor.execute("SELECT * FROM expenses WHERE id = ?",(id,))
        row=result.fetchone()
        if row is None:
            return False;
        else :
            return True;
    except Exception as e:
        print(e)
        input("Press Enter to Exit")
           