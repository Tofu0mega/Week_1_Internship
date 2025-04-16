from DB.dbconfig import init_db,get_conn,reset_schema
from Controllers.Transactions import Make_Transaction,View_Transaction_History,View_Transactions_By_Categories
from Controllers.Budgets import Define_Budget,View_Budget
import os
# import time
connection=get_conn()
# import msvcrt
exit_flag=True


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
reset_schema()
# init_db()
# def getch():
#     return msvcrt.getch().decode('utf-8')


def menu_display():
    cls()
    print("""
    1.Make Transaction
    2.View Transaction History
    3.Set Budget
    4.View Current Budget
    5.View Transaction By Categories with Budgeting
    6.Exit
    """)


def Handler(key):
    global exit_flag
    if key == '1':
        Make_Transaction()
    elif key == '2':
        View_Transaction_History()
    elif key == '3':
       Define_Budget()
    elif key == '4':
        View_Budget()
    elif key == '5':
       View_Transactions_By_Categories()
    elif key == '6':
        print("Commiting any Pending Transactions")
        connection.commit()
        print("Commited...Exiting")
        exit_flag=False
        
    else:
        print("Invalid Input please use numbers from 1 to 6")
        input("Press Enter to Continue")
    

def main():
    while(exit_flag):
        menu_display()
        # print("Enter Your Choice")
        key=input("Enter Your Choise (1-6)")
        Handler(key)
        
if __name__ == "__main__":
   main()
