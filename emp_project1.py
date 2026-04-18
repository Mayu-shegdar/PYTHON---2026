class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class EmployeesManager:
    def __init__(self):
        self.employees = []

    # Add employee
    def add_employee(self, employee):
        self.employees.append(employee)

    # List employees
    def list_employees(self):
        if not self.employees:
            print("No employees found")
        for emp in self.employees:
            print(emp)

    # Delete employees by age range
    def delete_employees_by_age_range(self, age_from, age_to):
        self.employees = [emp for emp in self.employees if not (age_from <= emp.age <= age_to)]
        print("Employees deleted in given age range")

    # Find employee by name
    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    # Update salary
    def update_salary_by_name(self, name, new_salary):
        emp = self.find_employee_by_name(name)
        if emp:
            emp.salary = new_salary
            print("Salary updated")
        else:
            print("Employee not found")


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def run(self):
        while True:
            print("\nEmployee Management System")
            print("1. Add Employee")
            print("2. List Employees")
            print("3. Delete Employees by Age Range")
            print("4. Find Employee by Name")
            print("5. Update Employee Salary")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                salary = float(input("Enter salary: "))
                emp = Employee(name, age, salary)
                self.manager.add_employee(emp)

            elif choice == "2":
                self.manager.list_employees()

            elif choice == "3":
                age_from = int(input("Enter age from: "))
                age_to = int(input("Enter age to: "))
                self.manager.delete_employees_by_age_range(age_from, age_to)

            elif choice == "4":
                name = input("Enter name to search: ")
                emp = self.manager.find_employee_by_name(name)
                print(emp if emp else "Employee not found")

            elif choice == "5":
                name = input("Enter name: ")
                new_salary = float(input("Enter new salary: "))
                self.manager.update_salary_by_name(name, new_salary)

            elif choice == "6":
                print("Exiting program")
                break

            else:
                print("Invalid choice")


# Run program
app = FrontendManager()
app.run()