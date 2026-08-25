# ATM Simulator	PIN login, deposit, withdrawal, and balance checking.
import time


Atm = {
    "Card_no" : 1234321,
    "name" : "Anone",
    "Amount" : 500,
    "pin" : 123,
    "DOB" : '00/00/0000'
}   



def change_pin(old_pin,new_pin):
    if Atm["pin"] == old_pin:
        Atm["pin"] = new_pin
        print("=== PIN CHANGE ===")

    else:
        print("Wrong pin...") 
        print("Press YES to Forgot pin..")

        choice = (input("ENTER YES OR NO.....")).strip().upper()

        if choice == "YES":
            forgot_pin()

            
            

def forgot_pin() :
    try:
        n = int(input("ENTER YOUR CARD NUMBER HERE.: "))
        m = (input("ENTER YOUR DOB HERE (xx/xx/xxxx).: "))          

        if Atm["Card_no"] == n  and Atm["DOB"] == m:

            o = int(input("ENTER YOUR NEW PIN HERE .: "))

            Atm["pin"] = o
            print("\n===PIN CHANGE===")

        else:
            print("Invalid card_no or DOB..")    

    except ValueError:
        print("Please enter the valid number...")   

             


def Check_balance():

    for i in range(1,4):
        try:
            pin = int(input("ENTER YOU PIN HERE.: "))
        except ValueError:
            print("please enter the valid pin")
            continue

        if Atm["pin"] == pin:
            print(f"\nYour Balance is RS.{Atm["Amount"]}")  
            break
        elif i >= 3:
            print("\nWRONG PIN.. ACCOUNT ASCESS BLOCKED..")          

        else:
            if i <  3:
                print(f"\nWrong Pin..{4-(i+1)} Attemp left.")       



def withdraw_balance():

    for i in range(1,4):
        try:
            pin = int(input("ENTER YOUR PIN HERE.: "))
            amount = float(input("ENTER THE AMOUNT TO WITHDRAWL.: "))
        except ValueError:
            print("Please enter the valid number.")
            continue

        if Atm["pin"] == pin:
            if amount <= Atm["Amount"]:
                Atm["Amount"] -= amount
                print(f"\nAmount Withdrawl Sucessful. Remaning balance is RS.{Atm["Amount"]:.2f}")
                break

            else:
                print(f"\nAccount balance low ... current balance is {Atm["Amount"]:.2f}") 
                break   

        elif i >= 3:
            print("\nWRONG PIN.. ACCOUNT ASCESS BLOCKED..")          

        else:
            if i <  3:
                print(f"\nWrong Pin..{4-(i+1)} Attempt left")       

                
            

def deposite_balance():

    for i in range(1,4):
        try:
            pin = int(input("ENTER YOUR PIN HERE.: "))
            amount = float(input("ENTER THE AMOUNT TO DEPOSITE.: "))
        except ValueError:
            print("Please enter the valid number.")
            continue

        if Atm["pin"] == pin:
            if amount > 0:
                Atm["Amount"] += amount
                print(f"\nAmount Deposite Sucessful. Remaning balance is RS.{Atm["Amount"]:.2f}")
                break

            else:
                print(f"\nDeposite ammount is invalid . cannot deposite nagative ammount.") 
                break   

        elif i >= 3:
            print("\nWRONG PIN.. ACCOUNT ASCESS BLOCKED..")          

        else:
            if i <  3:
                print(f"\nWrong Pin..{4-(i+1)} Attempt left")       

    

 


print("====================================")
print("         WELCOME TO THE ATM         ")
print("====================================")



card = int(input("\nPress ENTER to insert your ATM CARD..."))
print("\nReading card... Plaese wait.")
time.sleep(2)

if card == Atm["Card_no"]:
    print("\n--------------------------------------")
    print(f"welcome,{Atm["name"]}")
    print(f"Account Number: {Atm["Card_no"]}")                          
    print("----------------------------------------")

    

    while True:
        print("\nPlease choose an option")
        print("1. Check Balance")
        print("2. Deposite Money")
        print("3. Withdeaw Money")
        print("4. Change pin")
        print("5. Log Out")

        choice = input("\nENTER THE CHOICE FROM (1 TO 5)").strip()

        if choice == "1":
            Check_balance()

        elif choice == "2":
            deposite_balance()

        elif choice == "3":
            withdraw_balance()

        elif choice == "4":
            try:
                n = int(input("ENTER YOUR OLD PIN HERE.."))
                m = int(input("ENTER YOUR NEW PIN HERE"))
                change_pin(n,m)
            except ValueError:
                print("[ERROE] Invalid input. Please enter a valid number.")    

        elif choice == "5":
            print(f"\n Thank you for using our ATM, {Atm["name"]}. Goodbye!")
            break                
        else:
            print("[ERROR] Invalid selecation. Please choose a number from 1 to 4")

else:
    forgot_pin()            

