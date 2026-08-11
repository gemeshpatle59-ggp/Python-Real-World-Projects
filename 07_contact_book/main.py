import json
import os


contact_book = {
    "gemesh" : 9175142374
}


def load_data():
    global contact_book
    if os.path.exists("contact_book.json"):
        with open ("contact_book.json","r") as file:
            contact_book = json.load(file)

    else :
        save_contact()        

def save_contact():
    with open ("contact_book.json","w") as file:
        json.dump(contact_book,file,indent=4)

def Add_contact(name,number):
    print("\n---------------------------")
    contact_book[name] = number
    print("-----New Contact Added-----")
    print("---------------------------")
    print(f"{name} : {number}\n")


def search_contact(name):
    for item,number in contact_book.items():
        if item.lower().replace(" ","") == name.lower().replace(" ",""):
            print("\n-----Contact Found-----")
            print(f"{item} : {number}\n")
            return

    
    print("\n----Contack is Not in ContactBook---\n")    



def update_contact(name,new_name,number):

    if not contact_book:
        print("\nContact Book is empty.\n")
        return

    for key in contact_book:
        if key.lower().replace(" ","") == name.lower().replace(" ",""):
            contact_book.pop(key)

            contact_book[new_name] = number

            print("\n-----Contact Updated-----\n") 
            return
    print("\nContact not found======\n")           

def delete_contact():
    for i,(name,value) in enumerate (contact_book.items() , start=1):
        print(f"{i}.{name} : {value}")

    try:    
        n = int(input("Enter the contack number here to delete.: "))

        if 1 <= n <= len(contact_book):
            key_list = list(contact_book.keys())
            keys = key_list[n-1]

            contact_book.pop(keys)       
            print(f"{keys} contact is delete from contackbook")

        else:
            print("\nEnter a valid contac number.")   

    except ValueError:
        print("enter proper contact index number..")

load_data()

print("\n","="*30)
print(" =","CONTACK_BOOK".center(26),"=")
print("","="*30)    


while True:
    print("1. To Add Contact TO ContactBook..")
    print("2. To Search Contact in Contactbook..")
    print("3. To Update Contact of Contactbook..")
    print("4. TO Delete Contact of Contactbook..")
    print("5. To Exit..")


    try: 
        choice = int(input("Enter your choice from ( 1 to 5) here..: "))
    except ValueError:
        print("\n====enter proper choice..=====\n")
        continue

    if choice == 1:
        n = input("Enter the Name of contact here.: ")
        m = int(input("Enter the number of contact here.: "))
        Add_contact(n,m)
        save_contact()

    elif choice == 2:
        n = input("Enter contact name to search in contact book.: ")
        search_contact(n)

    elif choice == 3:
        n = input("Enter contact name which you want to update.: ") 
        m = input("Enter new contact name.: ")
        o = int(input("Enter the new contact numbmber,: "))

        update_contact(n,m,o)
        save_contact()

    elif choice == 4:


        delete_contact()
        save_contact()

    elif choice == 5:
        print("\n=========================")
        print("===Contact book closed===")    
        print("=========================\n")
        break

    else:
        print("something went wrong Enter choice from (1 to 5).")    

            
