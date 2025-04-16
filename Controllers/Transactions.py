from DB.dbconfig import get_conn, get_cursor
from DB.DB_Operations import Add_Transaction, getalltransaction,getamount_by_category
import os
import json
categories_path ="data/allowed_categories.json"
with open(categories_path, "r") as f:
    category_data = json.load(f)
    allowed_categories = category_data["categories"]
cursor=get_cursor()
connection=get_conn()


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def Make_Transaction():
    cls()
   
    print("Transaction Screen")
    print("Enter Transaction Details:")
    name=input("Enter Transaction Name: ")
    while(True):        
        amount=input("Enter Transaction Amount(in NRS): ")
        if amount.isdigit() and int(amount) > 0:
                
                break
        else:
                print("Invalid Input Try again")
                
    for i in range(0,len(allowed_categories)):
        print(i+1,allowed_categories[i])
    while(True):        
        cataindex=input(f"Enter Category Type:(1-{len(allowed_categories)}): ")
        if cataindex.isdigit() and 1 <= int(cataindex) <= len(allowed_categories):
            category=allowed_categories[int(cataindex)-1]
            break
        else:
            print("Invalid Input Try again")
    Transaction = {
    "name": name,
    "amount": amount,
    "category": category
    }
    Add_Transaction(Transaction)
    cls()
    print("The following Transaction has been added",Transaction)
    input("Press Enter to continue ....")


def View_Transaction_History():
    cls()
    print("Transaction History:")
    print(getalltransaction())
    input("Press Enter to continue...")

    
def View_Transactions_By_Categories():
    cls()
    print("Transactions by Categories")   
    print(getamount_by_category())
    input("Press Enter to Continue")            
    
    
    
  