class BankAccount:
    def __init__(self,name,balance,accountno):
        self.__balance = balance
        self.name = name
        self.accountno = accountno

    def deposit(self,D):
        try:
            D = int(D)
        
            if D > 0:
                self.__balance += D
                print(
                     f"\namount has been deposited to {self.name}Account ," 
                     f"current balance is  ₹{self.__balance}")
                print("\n..")
            else:
                print(f"invalid amount")    
                print("\n..")
        except ValueError:
                print("Invalid Amount")
                return
    def withdraw(self,D):
        try:
            D = int(D)
            if D <= 0:
                print("Invalid Amount")
                return
            
            if D <= self.__balance :
                self.__balance -= D
                print(f"\nrs{D} has been debited , balance is {self.__balance}")
                print("\n...")
            else:
                print(f"Low Balance to pay {D}rs Amount")
                print("\n..")
        except ValueError:
                    print("Invalid Amount")
                    return    
    def check_balance(self):
        print(f"the balance is {self.__balance}Rs")     
        print("\n..")

a1 = BankAccount("Gemesh",0,12321)


print("\n==============================================")
print("==========WELCOME TO YOUR BANK==================")
print("================================================")
print("\n...")

try:
    l = int(input("Enter your Account no.."))
except ValueError:
    print("Invalid Account No..")
    exit()    

if l == a1.accountno:
    print("\n-----------------------------------")
    print(f"Welcome Account Holder {a1.name}")
    print(f"Account number {l}")
    print("\n-----------------------------------")

else:
    print("Account number not found ,Please enter valid account number")    
    exit()

while True:
    print("\n1. TO Deposit the Amount......")
    print("2. To Withdraw the Amount......")
    print("3. To Check your balance.......")
    print("4. To Exit")

    print("\n Choose from (1 to 4)....")     

    choice = (input("\nEnter choice (1-4): "))   

    if choice == "1":
        d = input("Enter amount to deposite : ")
        a1.deposit(d)
    

    elif choice == "2":
        d = input("Enter amount to withdraw : ")
        a1.withdraw(d)

    elif choice == "3":
        a1.check_balance()

    elif choice == "4":
        print("\n========================")
        print("--------Thank you-------")
        print("========================")
        break

    else :
        print("\nInvalid Choice")
    

# a1.deposite(d)
