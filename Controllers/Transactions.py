from DB.dbconfig import get_conn, get_cursor
from DB.DB_Operations import Add_Transaction, getalltransaction,getamount_by_category,display_table,getalltransactionmnth,delete_record,edit_record,check_record,Get_categories
import os
import json



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def Make_Transaction():
    allowed_categories=Get_categories();
    cls()
   
    print("Transaction Screen")
    print("Enter Transaction Details:")
    name=input("Enter Transaction Name(# to back to main menu): ")
    if(name=='#'):
        return
    while(True):        
        amount=input("Enter Transaction Amount(in NRS)(# to back to main menu): ")
        if(amount=='#'):
            return
        elif amount.isdigit() and int(amount) > 0:
                
                break
        else:
                print("Invalid Input Try again")
                
    for i in range(0,len(allowed_categories)):
        print(i+1,allowed_categories[i])
    while(True):        
        cataindex=input(f"Enter Category Type:(1-{len(allowed_categories)})(# to back to main menu): ")
        if(cataindex=='#'):
            return
        elif cataindex.isdigit() and 1 <= int(cataindex) <= len(allowed_categories):
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
    display_table(getalltransaction())
    input("Press Enter to continue...")

    
def View_Transactions_By_Categories():
    cls()
    print("Transactions by Categories")   
    display_table(getamount_by_category(),Status=True)    
    input("Press Enter to Continue")            
    
    
def View_This_Mnths_Transactions():
    cls()
    print("This Months Transactions")
    display_table(getalltransactionmnth())
    input("Press Enter to Continue")

def Delete_Transaction():
    cls()
    print("Choose a Transaction to Delete")
    display_table(getalltransaction())
    while(True):
        targetid=input('Enter Id to Delete (# to back to main menu): ')
        if(targetid=='#'):
            return
        elif(delete_record(targetid) == 1):
            print("Record Deleted")
            input("Press Enter To Continue")
            break
        
        else:
            print("No Record with that Id or Invalid Input")
            input("Press Enter to Continue")
    
    
    
    
def Edit_Transaction():
    allowed_categories=Get_categories();
    cls()
    print("Choose a Transaction to Edit")
    display_table(getalltransaction())
    while(True):
        
        targetid=input('Enter Id to Edit (# to back to main menu): ')
        if(targetid=='#'):
            return
        elif(check_record(targetid)):
            break
        else:
            print("Invalid Input or No Record with Such Id")
            input("Hit Enter to Continue")
    cls()
    name=input("Enter Transaction Name (# to back to main menu): ")
    if(name=='#'):
        return
    while(True):        
        amount=input("Enter Transaction Amount(in NRS)(# to back to main menu): ")
        if(amount=='#'):
            return
        if amount.isdigit() and int(amount) > 0:
                
                break
        else:
                print("Invalid Input Try again")
                
    for i in range(0,len(allowed_categories)):
        print(i+1,allowed_categories[i])
    while(True):        
        cataindex=input(f"Enter Category Type:(1-{len(allowed_categories)})(# to back to main menu): ")
        if(cataindex=='#'):
            return
        elif cataindex.isdigit() and 1 <= int(cataindex) <= len(allowed_categories):
            category=allowed_categories[int(cataindex)-1]
            break
        else:
            print("Invalid Input Try again")
    Transaction = {
    "name": name,
    "amount": amount,
    "category": category,
    "id":targetid
    }
    edit_record(Transaction)
    
    