from DB.dbconfig import init_db,get_conn,reset_schema
from Controllers.Transactions import Make_Transaction,View_Transaction_History,View_Transactions_By_Categories,View_This_Mnths_Transactions,Delete_Transaction,Edit_Transaction
from Controllers.Budgets import Define_Budget,View_Budget,Add_Category,Delete_Category

import os
from dotenv import load_dotenv
load_dotenv()
load_dotenv()
print("Loaded environment:", os.getenv('State'))

# import time
connection=get_conn()
# import msvcrt
exit_flag=True


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


enviroment=os.getenv('State','Demo')

def loaddbstates(enviroment):
    print("Running in ",enviroment,"mode")
    input("Press Enter to Start")

        
       
    if(enviroment=='Development'):
        reset_schema()
        init_db()
    elif(enviroment=='Clean'):
        reset_schema()
    else:
        init_db()

loaddbstates(enviroment)

def menu_display():
    cls()
    print("""
    💰💰Expense Trackng System💰💰
        0.Make Transaction
        1.Edit Transaction
        2.Delete Transaction
        3.View This Months Transaction
        4.View Transaction History
        5.Set Budget
        6.View Current Budget
        7.View Transaction By Categories with Budgeting   
        8.Add Category   
        9.Delete Category
        #.Exit
    """)


def Handler(key):
    global exit_flag
    if key == '0':
        Make_Transaction()
    elif key =='1':
        Edit_Transaction()
    elif key =='2':        
        Delete_Transaction()
    elif key == '3':
        View_This_Mnths_Transactions()
    elif key == '4':
        View_Transaction_History()
    elif key == '5':
       Define_Budget()
    elif key == '6':
        View_Budget()
    elif key == '7':
       View_Transactions_By_Categories()
    elif key =='8':
        Add_Category()
    elif key == '9':
        Delete_Category()
    elif key == '#':
        print("Commiting any Pending Transactions")
        connection.commit()
        print("Commited...Exiting")
        exit_flag=False
        
    else:
        print("Invalid Input")
        input("Press Enter to Continue")
    

def main():
    while(exit_flag):
        menu_display()
        # print("Enter Your Choice")
        key=input("Enter Your Choise (1-9): ")
        Handler(key)
        
if __name__ == "__main__":
   main()
