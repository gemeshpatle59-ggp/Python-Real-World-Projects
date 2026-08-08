import os
import json


class Inventory:
    def __init__(self):
        if os.path.exists("inventory.json"):
            with open("inventory.json","r") as file:
                self.item = json.load(file)
        else:
            self.item = {}        

    def save_item(self):
        with open("inventory.json","w") as file:
            json.dump(self.item,file,indent=4)


    def add_item(self,item,quantity):    
        if item not in self.item:
            self.item[item] = quantity
            print(f"\n{item} : {quantity} is added to inventory")
            print("\n------------------------")

        else:
            print("item is already present in inventory")    
            print("\n------------------------")
            

    def remv_item(self,remv):
        if remv in self.item:
            self.item.pop(remv)
            print(f"\n{remv} is removed from inventory ")   
            print("\n------------------------")
                 

        else:
            print(f"\n{remv} is already not in inventory ")    
            print("\n------------------------")

    def updt_quty(self,item,quantity):
        if item in self.item:
            self.item[item] = quantity
            print(f"\n{item} qunatity is updaated to {quantity}") 
            print("\n------------------------")

        else:
            print(f"\n{item} is not in inventory")    
            print("\n------------------------")

    def search_item(self,item):
        if item in self.item:
            print("\nItem found") 
            print(f"item    = {item}")      
            print(f"quantityity = {self.item[item]}") 
            print("\n------------------------")

        else:
            print(f"\n{item} not in inventory ")    
            print("\n------------------------")

    def show_inventory(self):
        print("\n------ Inventory------")
        for item, quantity in self.item.items():
            
            print(f"\n{item} : {quantity}")
        print("\n------------------------")

    def show_low(self):
        # low = min(self.item, key=self.item.get)
        print("\n---Low Stock")
        if self.item:
            for item , quantityy in self.item.items():
                if quantityy < 5:
                    print(f"{item} : {self.item[item]}")
            print("\n------------------------")
        else:  
            print("inventory is empty")
            print("\n------------------------")

    def show_high(self):
        if self.item:
            hig = max(self.item, key=self.item.get)
            print("\n-----Highest Stock------")
            print(f"{hig} : {self.item[hig]}")
            print("\n------------------------")
        else:
            print("\nInventory is empty")
            print("\n------------------")

a1 = Inventory()

print("\n===========================================")
print("---------------Items Inventory-----------------")
print("=============================================")
print("\n...")

while True:
    print("1.To Add Item in Inventory")
    print("2.To Remove Item in Inventory")
    print("3.To Update Item in Inventory")
    print("4.To Search Item in Inventory")
    print("5.To Show Inventory")
    print("6.To Show Low Stock Items in Inventory")
    print("7.To Show Highest Stock Item in Inventory")
    print("8 To Exit")
    print("\n....")

    choice = input("Enter your choice from (1 to 8).")

    if choice == "1": 
        try:
            a = input("Enter item to add in inventory : ")
            b = int(input("enter quantityity of the item : "))
            a1.add_item(a,b)
            a1.save_item()
        except ValueError:
            print("enter quantity properly ")

    elif choice == "2":
                a = input("Enter item to remove in inventory : ")
                a1.remv_item(a)
                a1.save_item()
    elif choice == "3":
        try:
            a = input("Enter item to add in inventory : ")
            b = int(input("enter quantityity of the item : "))    

            a1.updt_quty(a,b)
            a1.save_item()
        except ValueError:
            print("enter quantity properly")

    elif choice == "4":
        a = input("Enter item to add in inventory : ")
        a1.search_item(a)

    elif choice == "5":
        a1.show_inventory()  

    elif choice == "6":
        a1.show_low()   

    elif choice == "7":
        a1.show_high()


    elif choice == "8":
        print("\n----------")    
        print("----Thank you ----")  
        print("\n-----------")  
        break
    else:            
        print("something went wrong")    
        
