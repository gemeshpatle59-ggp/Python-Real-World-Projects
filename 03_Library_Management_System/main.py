class Library:
    def __init__(self):                                                     
        self.books = {
            "python" : True,
            "java" : True,
            "C++" : False,
            "C"  : True
        }

    def add_book(self,add):
        self.books[add] = True
        # print(self.books)

    def borrow_book(self,brow):
        try:
            if brow not in self.books:
                print("book is not found")
            elif self.books[brow] == False:
                print("book is not available...")

            elif brow in self.books:
                self.books[brow] = False
                print("book has been borrowed...")
            else:
                print("Book not found..")
        except KeyError:
            print("something went wrong")

                        
    def remove_book(self,remv):

        if remv in self.books:
            self.books.pop(remv)
            print("the book has been removed..")
        else:
            print("Book is not in libreary..")


    def show_books(self):

        print("Available books")
        print("\n")
        for book , status in self.books.items():
            if status == True:
                print(book)

        print("\n Borrowed Books")    
            

        for book , status in self.books.items():
            if status == False:
                print(book)


    def return_book(self,retrn):
        try:
            if retrn not in self.books:
                print("this book has not been borrowed..")
            elif self.books[retrn] == True :
                print("book has not been borrowed so can't return..")
            else:
                self.books[retrn] = True
                print("the book has returned")

        except KeyError:
            print("enter correct book name...")         

a1 = Library()

print("\n========================================")
print("---------WELCOME TO LIBRARY---------------")
print("==========================================")
print("\n...")

while True:
    print("\n...")
    print("1.Add Book...")
    print("2.Remove Book...")
    print("3.Borrow Book...")
    print("4.Return Book...")
    print("5.Show Books...")
    print("6.Exit...")
    print("\n...")

    choice = input("Enter choice (1 to 6)...")

    try:
        if choice == "1":
            a = input("enter book to add..: ")
            a1.add_book(a)
            print("books has been added ")

        elif choice == "2":
            a = input("enter book to remove..: ")
            a1.remove_book(a)    

        elif choice == "3":
            a = input("enter book to borrow..: ")  
            a1.borrow_book(a)

        elif choice == "4":
            a = input("enter book to return..:")
            a1.return_book(a)    

        elif choice == "5":
            a1.show_books()

        elif choice == "6":
            print("-------Thank you-------")
            break
        else:
            print("something Went wrong")    
            
    except KeyError:
        print("something went wrong")        
