#Q2. Define an Employee class with attributes like name, ID, and salary. 
#Create a Manager subclass that includes a list of employees they manage. 
#Write methods to calculate bonuses and display employee details.

class employee:
    def __init__(self, name, ID, salary):
        self.name = name
        self.ID = ID
        self.salary = salary

    def calculate_bonuses(self, percentage):
        return self.salary *(percentage / 100)

    def display(self):
        return f"Name : {self.name},ID: {self.ID},Salary: {self.salary}"


class Manager(employee):
    def __init__(self, name, emp_id, salary):
        super().__init__(name, emp_id, salary)
        self.employees_managed =[]

    def add_employee(self, employee):
        self.employees_managed.append(employee)

    def remove_employee(self, emp_id):
        self.employees_managed = [
            emp for emp in self.employees_managed if emp.ID!= emp_id
        ]

    def display_team(self):
        print(f"\nManager {self.name} manages:")
        if not self.employees_managed:
            print("No employees under this manager.")
        else:
            for emp in self.employees_managed:
                emp.display()


mgr_name = input("Enter manager name: ")
mgr_id = input("Enter manager ID: ")
mgr_salary = float(input("Enter manager salary: "))
manager = Manager(mgr_name, mgr_id, mgr_salary)

num = int(input("How many employees do you want to add? "))
for i in range(num):
    print(f"\nEnter details for Employee {i+1}:")
    name = input("Name: ")
    emp_id = input("ID: ")
    salary = float(input("Salary: "))
    emp = employee(name, emp_id, salary)
    manager.add_employee(emp)

manager.display_team()

remove_id = input("\nEnter Employee ID to remove: ")
manager.remove_employee(remove_id)

manager.display_team()


