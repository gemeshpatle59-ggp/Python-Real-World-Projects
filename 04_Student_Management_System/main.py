class Students:
    def __init__(self):
        self.students = {
            "gemesh": 90
        }

    def remove_stud(self, stud):

        if stud in self.students:
            self.students.pop(stud)

            print(
                f"\n{stud} "
                "is removed"
                "\n"
            )

        else:
            print(
                "\nStudent is not in class"
                "\n"
            )

    def add_stud(self, stud, mark):

        if stud not in self.students:
            self.students[stud] = mark

            print(
                f"\n{stud} "
                "is added to the class"
                "\n"
            )

        else:
            print(
                f"\n{stud} "
                "is already in class"
                "\n"
            )

    def update_mark(self, stud, mark):

        if stud in self.students:
            self.students[stud] = mark

        else:
            print(
                "\nStudent is not in class"
                "\n"
            )

    def search_stud(self, stud):

        if stud in self.students:

            print(
                "\nStudent Found"
                f"\nName : {stud}"
                f"\nMark : {self.students[stud]}"
                "\n"
            )

        else:
            print(
                f"\n{stud} "
                "is not in class"
                "\n"
            )

    def showall_stud(self):

        print(
            "\n===================="
            "\n    STUDENT LIST"
            "\n===================="
        )

        for stud, mark in self.students.items():

            print(
                f"\nName : {stud}"
                f"\nMark : {mark}"
                "\n--------------------"
            )

    def show_topper(self):

        if not self.students:
            print("No students are available.")

        else:
            print(
                "\n===================="
                "\n TOPPER OF THE CLASS"
                "\n===================="
            )

            top = max(
                self.students,
                key=self.students.get
            )

            print(
                f"\nName : {top}"
                f"\nMark : {self.students[top]}"
                "\n"
            )


a1 = Students()


print(
    "\n======================"
    "\n== WELCOME TO CLASS =="
    "\n======================"
    "\n.."
)


while True:

    print(
        "\n1. To Add Student to Class"
        "\n2. To Remove Student From Class"
        "\n3. To Update Marks of Students"
        "\n4. To Search Student in Class"
        "\n5. To Show All Students in Class"
        "\n6. To See the Topper of Class"
        "\n7. To Exit"
        "\n..."
    )

    choice = input(
        "\nEnter your choice from (1 to 7): "
    )

    print(
        "\n========================================="
    )

    n = (
        "\n========================================="
    )


    try:

        if choice == "1":

            stud = input(
                "\nEnter a student name: "
            )

            mark = int(
                input(
                    "Enter student mark: "
                )
            )

            a1.add_stud(
                stud,
                mark
            )

            print(n)


        elif choice == "2":

            stud = input(
                "\nEnter name of student: "
            )

            a1.remove_stud(
                stud
            )

            print(n)


        elif choice == "3":

            stud = input(
                "\nEnter name of student: "
            )

            mark = int(
                input(
                    "Enter a mark to update: "
                )
            )

            if 0 <= mark <= 100:

                print(n)

                a1.update_mark(
                    stud,
                    mark
                )

                if stud in a1.students:

                    print(
                        f"\n{stud}'s "
                        "mark is updated"
                        "\n"
                    )

                print("\n...")

            else:

                print(
                    "\nMark must be between "
                    "0 and 100"
                    "\n....."
                )


        elif choice == "4":

            stud = input(
                "\nEnter name of student "
                "to search in class: "
            )

            print(n)

            a1.search_stud(
                stud
            )

            print(
                "\n....."
            )


        elif choice == "5":

            a1.showall_stud()

            print(
                "\n....."
            )


        elif choice == "6":

            a1.show_topper()

            print(
                "\n...."
            )


        elif choice == "7":

            print(
                "\n--------------"
                "\n-- THANK YOU --"
                "\n--------------"
            )

            break


        else:

            print(n)

            print(
                "\nSomething went wrong."
                "\nChoose a number from "
                "1 to 7."
            )

            print(n)


    except ValueError:

        print(n)

        print(
            "\nSomething went wrong."
            "\nPlease enter the "
            "correct value."
        )

        print(n)
