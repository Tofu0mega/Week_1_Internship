from DB.dbconfig import get_conn, get_cursor
from DB.DB_Operations import definebudget,getdefinedbudget,display_table,Get_categories,delete_category
import os

cursor=get_cursor()
connection=get_conn()



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def Define_Budget():
    allowed_categories=Get_categories();
    cls()
    print("Budget Screen")
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
    while(True):        
        amount=input(f"Enter Budget Amount for {category} (# to back to main menu):")
        if(amount=='#'):
            return
        if amount.isdigit() and int(amount) > 0:
                
                break
        else:
                print("Invalid Input Try again")    
         
    Transaction={
        "category": category,
        "amount":amount
    }
    definebudget(Transaction)
    print("Budget Defined for",Transaction)
    input("Press Enter to Continue")
    
def View_Budget():
    cls()
    print("Current Budget Listing")
    display_table(getdefinedbudget())
    input("Press Enter to Continue")
    
def Add_Category():
    cls()
    print(" New Category Screen")
    newcata=input("Enter New Category To Add  (# to return):")
    if newcata =='#':
        return
    if (newcata in Get_categories() ):
        print("Sorry Category Already Exists")
        input("Press Enter to Continue")
    else:
        while(True):        
            amount=input(f"Enter Budget Amount for {newcata} (# to back to main menu):")
            if(amount=='#'):
                return
            if amount.isdigit() and int(amount) > 0:
                    
                    break
            else:
                    print("Invalid Input Try again")    
            
    Transaction={
        "category": newcata,
        "amount":amount
    }
    definebudget(Transaction)
    print("Budget Defined for",Transaction)
    input("Press Enter to Continue")
    
def Delete_Category():
    cls()
    print("Current Budget Listing")
    display_table(getdefinedbudget())
    while(True):
        target_id=input("Enter id of Category to Delete (# to return to mainmenu):" )
        if(target_id=='#'):
            return
        elif(delete_category(target_id) == 1):
            print("Record Deleted")
            input("Press Enter to Continue")
            break
        else:
            print("No Record with that Id or Invalid Input")
            input("Press Enter to Continue")
