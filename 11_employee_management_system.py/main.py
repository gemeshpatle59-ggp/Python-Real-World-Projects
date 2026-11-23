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

