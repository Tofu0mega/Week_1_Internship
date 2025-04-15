from DB.dbconfig import init_db,get_conn
import time
connection=get_conn()
# import msvcrt
exit_flag=True

init_db()
# def getch():
#     return msvcrt.getch().decode('utf-8')


def menu_display():
    print("""
    1.Make Transaction
    2.View Transaction History
    3.Set Budget
    4.View Current Budget
    5.View Transaction By Categories
    6.Exit
    """)


def Handler(key):
    global exit_flag
    if key == '1':
        print("Make Transaction ")
    elif key == '2':
        print("View Transaction Historu")
    elif key == '3':
        print("Set Budget")
    elif key == '4':
        print("View Current Budget")
    elif key == '5':
        print("View Transaction By Category")
    elif key == '6':
        print("Commiting any Pending Transactions")
        connection.commit()
        print("Commited...Exiting")
        exit_flag=False
        
    else:
        print("Invalid Input please use numbers from 1 to 6")
    

def main():
    while(exit_flag):
        menu_display()
        # print("Enter Your Choice")
        key=input("Enter Your Choise (1-6)")
        Handler(key)
        
if __name__ == "__main__":
   main()
