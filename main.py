from DB.dbconfig import init_db,get_conn,reset_schema
from Controllers.Transactions import Make_Transaction,View_Transaction_History,View_Transactions_By_Categories,View_This_Mnths_Transactions,Delete_Transaction,Edit_Transaction
from Controllers.Budgets import Define_Budget,View_Budget
from Controllers.Seeder import seed_data
import os
from dotenv import load_dotenv
load_dotenv()
# import time
connection=get_conn()
# import msvcrt
exit_flag=True


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


enviroment=os.getenv('State','Demo')

def loaddbstates(enviroment):
    if(enviroment=='Testing'):
        reset_schema()
        seed_data()
    elif(enviroment=='Development'):
        reset_schema()
    else:
        init_db

loaddbstates(enviroment)

def menu_display():
    cls()
    print("""
    💰💰Expense Trackng System💰💰
        1.Make Transaction
        2.Edit Transaction
        3.Delete Transaction
        4.View This Months Transaction
        5.View Transaction History
        6.Set Budget
        7.View Current Budget
        8.View Transaction By Categories with Budgeting        
        9.Exit
    """)


def Handler(key):
    global exit_flag
    if key == '1':
        Make_Transaction()
    elif key =='2':
        Edit_Transaction()
    elif key =='3':
        
        Delete_Transaction()
    elif key == '4':
        View_This_Mnths_Transactions()
    elif key == '5':
        View_Transaction_History()
    elif key == '6':
       Define_Budget()
    elif key == '7':
        View_Budget()
    elif key == '8':
       View_Transactions_By_Categories()
    elif key == '9':
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
