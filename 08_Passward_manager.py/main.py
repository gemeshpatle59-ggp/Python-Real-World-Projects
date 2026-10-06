# Password Manager	Save and search passwords securely in a simple project.

import string
import json
import os
from secrets import choice
from cryptography.fernet import Fernet


if not os.path.exists("secret.key"):
    key = Fernet.generate_key()

    with open("secret.key", "wb") as file:
        file.write(key)

master_passward = "demo_password"

password_manager = []

def load_key():
    with open("secret.key","rb") as file:
        return file.read()

key = load_key()
fernet = Fernet(key)    

def check_master_passward():
    password = input("ENTER MASTER PASSWARD: ")

    if password == master_passward:
        return True

    return False

if not check_master_passward():
    print("WRONG MASTER PASSWARD.")
    exit()


def load_file():
    global password_manager
    if os.path.exists("password_manager.json"):
        with open ("password_manager.json","r") as file:
            password_manager = json.load(file)

    else:
        save_password()


def save_password():
    with open("password_manager.json","w") as file:
        json.dump(password_manager,file,indent=4)                


def add_password(name,username,password):    

    encrypted_password = fernet.encrypt(password.encode()).decode()

    password_manager.append({
        "website/app"    : name,
        "username/email" : username,
        "password"       : encrypted_password
    })
    print("\n======USEARNAME PASSWORD ADDED======\n")


def Search_pasward(name):
    for names in password_manager:
        if names["website/app"].lower().replace(" ","") == name.lower().replace(" ",""):
            print("\n=====password FOUND=====")
            print(f"website/app    : {names["website/app"]}")
            print(f"username/email : {names["username/email"]}")
            decrypted_passward = fernet.decrypt(names["password"].encode()).decode()
            print(f"password       : {decrypted_passward}")
            return

    print("\n=====PASSWORD NOT FOUND=====\n")    


def view_all():
    print("\n========ALL PASSWORDS========")

    for names in password_manager:
        print(f"\nwebsite/app    : {names["website/app"]}")
        print(f"username/email : {names["username/email"]}")
        decrypted_passward = fernet.decrypt(names["password"].encode()).decode()
        print(f"password       : {decrypted_passward}\n")

def delete_password(name):
    for names in password_manager:
        if names["website/app"].lower().replace(" ","") == name.lower().replace(" ",""):
            password_manager.remove(names)
            print("PASSWORD DELETED SUCCESSFULLY")
            return
    print("======PASSWORD NOT FOUND======")    

def password_generator():
    try:
        n = int(input("ENTER TEH LENGTH OF THE PASSWORD.: "))

    except ValueError:
        print("please enter the valid length.")    
        return None
    if n <= 0:
        print("Password length must be greater than 0.")
        return None
        
    password = ""

    for i in range(n):
        password += choice(string.ascii_letters + string.digits + string.punctuation)

    return password

load_file()

print("\n","="*30)
print("PASSWORD MANAGER".center(30))
print("","="*30)

while True:
    print("1. TO ADD PASSWORD.")
    print("2. TO SEARCH PASSWORD.")
    print("3. TO VIEW ALL PASSWORD.")
    print("4. TO DELETE PASSWORD")
    print("5. TO GENERATE PASSWORD.")
    print("6. TO Exit..")

    try:
        user_choice = int(input("Enter your user_choice (1 to 6).: "))

        if user_choice == 1:
            n = input("ENTER THE WEBSITE/APP NAME HERE.: ")
            m = input("ENTER YOUR USERNAME/EMAIL HERE.: ")
            password_type = input("ENTER PASSWORD MANUALLY PT GENERATE ? (m/g): ")

            if password_type == "g":
                o = password_generator()
                print(f"Generated Password: {o}")

                use_password = input("YOU WANT TO USE THIS PASSWARD.(y/n): ")  

                if use_password != "y":
                    print("passward discarded.")
                    continue

            else:
                o = input("ENTER YOUR PASSWARD HERE.: ") 
                 

            add_password(n,m,o)
            save_password()

        elif user_choice == 2:
            n = input("ENTER THE WEBSITE/APP NAME TO SEARCH PASSWARD.: ")
            Search_pasward(n)

        elif user_choice == 3:
            view_all()

        elif user_choice == 4:
            n = input("ENTER THE NAME OF THE WEBSITE/APP TO DELETE ITS PASSWARD FROM PASWARD MANAGER.: ")

            delete_password(n)
            save_password()

        elif user_choice == 5:
            print(password_generator())

        elif user_choice == 6:
            break

        else:
            print("\nPLEASE ENTER THE PROPER user_CHOICE FROM (1 to 6).")

    except ValueError:
        print("PLEASE ENTER VALID user_CHOICE .")      

                      