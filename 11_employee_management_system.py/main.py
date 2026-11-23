# Employee Management System Manage employee details, roles, and salaries

import json
import os


class EmployeeManagement:

    def __init__(self):
        self.filename = "employees.json"
        self.employees = self.load_data()

    # Load JSON data
    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, OSError):
                print("Error loading data. Starting with empty records.")

        return {}

# Save JSON data
    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.employees, file, indent=4)

   # Add Employee
    def add_employee(self):

        emp_id = input("Enter Employee ID: ").strip()

        if not emp_id:
            print("Employee ID cannot be empty.")
            return

        if emp_id in self.employees:
            print("Employee ID already exists!")
            return

        name = input("Enter Name: ").strip()
        age = input("Enter Age: ").strip()
        department = input("Enter Department: ").strip()
        designation = input("Enter Designation: ").strip()
        salary = input("Enter Salary: ").strip()
        phone = input("Enter Phone Number: ").strip()
        joining_date = input("Enter Joining Date: ").strip()

        if not all([name, age, department, designation,
                    salary, phone, joining_date]):
            print("All fields are required!")
            return

        try:
            age = int(age)
            salary = float(salary)

            if age <= 0 or salary < 0:
                print("Invalid age or salary!")
                return

        except ValueError:
            print("Age and salary must be numeric!")
            return

        self.employees[emp_id] = {
            "name": name,
            "age": age,
            "department": department,
            "designation": designation,
            "salary": salary,
            "phone": phone,
            "joining_date": joining_date,
            "attendance": {
                "present": 0,
                "absent": 0,
                "leave": 0
            }
        }

        self.save_data()
        print("Employee added successfully!")

    # View All Employees
    def view_employees(self):

        if not self.employees:
            print("No employee records found!")
            return

        for emp_id, emp in self.employees.items():

            print("\n------------------------------")
            print("Employee ID :", emp_id)
            print("Name        :", emp["name"])
            print("Age         :", emp["age"])
            print("Department  :", emp["department"])
            print("Designation :", emp["designation"])
            print("Salary      :", emp["salary"])
            print("Phone       :", emp["phone"])
            print("Joining Date:", emp["joining_date"])
            print("Attendance  :", emp["attendance"])

    # Search Employee
    def search_employee(self):

        emp_id = input("Enter Employee ID: ").strip()

        if emp_id in self.employees:
            print("\nEmployee Found!")
            print(self.employees[emp_id])
        else:
            print("Employee not found!")

    # Update Employee
    def update_employee(self):

        emp_id = input("Enter Employee ID: ").strip()

        if emp_id not in self.employees:
            print("Employee not found!")
            return

        emp = self.employees[emp_id]

        print("""
1. Name
2. Age
3. Department
4. Designation
5. Salary
6. Phone
7. Joining Date
""")

        choice = input("Select field to update: ").strip()

        fields = {
            "1": "name",
            "2": "age",
            "3": "department",
            "4": "designation",
            "5": "salary",
            "6": "phone",
            "7": "joining_date"
        }

        if choice not in fields:
            print("Invalid choice!")
            return

        field = fields[choice]
        new_value = input(f"Enter new {field}: ").strip()

        if not new_value:
            print("Value cannot be empty!")
            return

        try:
            if field == "age":
                new_value = int(new_value)
                if new_value <= 0:
                    raise ValueError

            elif field == "salary":
                new_value = float(new_value)
                if new_value < 0:
                    raise ValueError

        except ValueError:
            print("Invalid numeric value!")
            return

        emp[field] = new_value

        self.save_data()
        print("Employee updated successfully!")

    # Delete Employee
    def delete_employee(self):

        emp_id = input("Enter Employee ID: ").strip()

        if emp_id not in self.employees:
            print("Employee not found!")
            return

        confirm = input("Are you sure? (yes/no): ").lower()

        if confirm == "yes":
            del self.employees[emp_id]
            self.save_data()
            print("Employee deleted successfully!")
        else:
            print("Deletion cancelled!")

    # Salary Management
    def salary_management(self):

        emp_id = input("Enter Employee ID: ").strip()

        if emp_id not in self.employees:
            print("Employee not found!")
            return

        emp = self.employees[emp_id]

        monthly = emp["salary"]
        yearly = monthly * 12

        print("\nSalary Report")
        print("Employee:", emp["name"])
        print("Monthly Salary:", monthly)
        print("Yearly Salary:", yearly)

    # Attendance Management
    def attendance_management(self):

        emp_id = input("Enter Employee ID: ").strip()

        if emp_id not in self.employees:
            print("Employee not found!")
            return

        emp = self.employees[emp_id]

        print("""
1. Present
2. Absent
3. Leave
""")

        choice = input("Select attendance: ").strip()

        options = {
            "1": "present",
            "2": "absent",
            "3": "leave"
        }

        if choice not in options:
            print("Invalid choice!")
            return

        status = options[choice]

        emp["attendance"][status] += 1

        self.save_data()
        print("Attendance marked successfully!")

    # Employee Statistics
    def statistics(self):

        if not self.employees:
            print("No employee records!")
            return

        salaries = [
            emp["salary"]
            for emp in self.employees.values()
        ]

        departments = set(
            emp["department"]
            for emp in self.employees.values()
        )

        print("\n========== STATISTICS ==========")

        print("Total Employees:", len(self.employees))
        print("Total Departments:", len(departments))
        print("Average Salary:", sum(salaries) / len(salaries))
        print("Highest Salary:", max(salaries))
        print("Lowest Salary:", min(salaries))

        print("\nDepartment-wise Employees:")

        for department in departments:
            count = sum(
                1 for emp in self.employees.values()
                if emp["department"] == department
            )
            print(department, ":", count)

    # Main Menu
    def run(self):

        while True:

            print("""
====================================
       EMPLOYEE MANAGEMENT SYSTEM
====================================

1. Add Employee
2. View All Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Salary Management
7. Attendance Management
8. Employee Statistics
9. Exit

====================================
""")

            choice = input("Enter Your Choice: ").strip()

            if choice == "1":
                self.add_employee()

            elif choice == "2":
                self.view_employees()

            elif choice == "3":
                self.search_employee()

            elif choice == "4":
                self.update_employee()

            elif choice == "5":
                self.delete_employee()

            elif choice == "6":
                self.salary_management()

            elif choice == "7":
                self.attendance_management()

            elif choice == "8":
                self.statistics()

            elif choice == "9":
                self.save_data()
                print("Thank you for using EMS!")
                break

            else:
                print("Invalid choice! Try again.")


# Run Application
if __name__ == "__main__":

    app = EmployeeManagement()
    app.run()