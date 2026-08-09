# TO_DO LIST .......


import json
import os

To_do = {
    "learn python" : True,
    "Hit GYM" : False
}

def load_data():
    global To_do

    if os.path.exists("To_do.json"):
        with open("To_do.json", "r") as file:
            To_do = json.load(file)

    else:
        save_data()

def save_data():
    with open("To_do.json","w") as file:
        json.dump(To_do,file,indent=4)

def Add_task(task):
    To_do[task] = False
    print("\nNew Task Is Added.")

def remove_task():
    try:
        for i ,(key , status) in enumerate (To_do.items() , start=1):
            print(f"{i}.{key} : {status}")
        n = int(input("enter task no. you want to remove.: "))
        task_list = list(To_do.keys())
        tasks = task_list[n - 1]
        To_do.pop(tasks) 
        print(f"\ntask {tasks} is removed..") 

    except ValueError:
        print("check proper numbering of tasks..")      

def Update_task():
    try:
        for i,(key,status) in enumerate (To_do.items(),start=1):
            print(f"{i}.{key} : {status}")
        n = int(input("enter task no. you want to update.: "))

        task_list = list(To_do.keys())
        tasks = task_list[n - 1]
        To_do[tasks] = True
        print("\n Task is completed..")

    except ValueError:
        print("check proper numbering of tasks")
def Show_all_task():
    print("\n====All Tasks=====\n")    

    if not To_do:
        print("\nNo Tasks available.")
        return
    
    for i ,(task, status) in enumerate (To_do.items() , start=1):
        print(f"{i}.{task} : {status}")
    print("\n..")

def show_pending_task():
    print("\n====Pending Tasks====")
    for i , (task, status) in enumerate ( To_do.items(), start=1):
        if status == False:
            print(f"{i}.{task} : {status}")
    print("\n..")

def Completed_task():
    print("\n====Completed Task====")
    for i, (task, status) in enumerate (To_do.items(),start=1):
        if status == True:
            print(f"{i}.task = {task}")
            print(f"  status = {status}\n")
    print("\n..")

def search_task(task):
    tsk = ""
    for tasks , status in To_do.items():
            if tasks.lower().replace(" ","") == task.lower().replace(" ",""):
                print("\n====Task Found====\n.")
                print(f"task = {tasks}")
                print(f"status = {status}")

    for tasks , status in To_do.items():
        keys = tasks.lower().replace(" ","")
        tsk += keys
    if task.lower().replace(" ","") not in tsk:
        print("task is not in list..")
    

                


print("="*20)
print("To-Do LIST".center(20))
print("="*20)
print("\n..")

load_data()


while True:

    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. Show All Tasks")
    print("5. Show Pending Tasks")
    print("6. Show Completed Tasks")
    print("7. Search Task")
    print("8. Exit\n")

    try:
        choice = int(input("Enter your Choice from ( 1 to 8 ) : "))

        if choice == 1:
            n = (input("Enter task to add..: "))
            Add_task(n)
            save_data()

        elif choice == 2:
            remove_task()    
            save_data()

        elif choice == 3:
    
            Update_task()    
            save_data()

        elif choice == 4:
            Show_all_task()

        elif choice == 5:
            show_pending_task()

        elif choice == 6:
            Completed_task()

        elif choice == 7:
            n = (input("ENter the task ..: "))
            search_task(n)         

        elif choice == 8:
            print("======Thank you=====") 
            print("----TO-DO list is closed---")   
            break

        else:
            print("Something went wrong..")
    except ValueError:
        print("Something Went wrong..")



