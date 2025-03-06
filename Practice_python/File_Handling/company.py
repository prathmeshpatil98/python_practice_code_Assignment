from Employee import Employee1

class Company:
    def __init__(self):
        self.employees = []  

    def add_employee(self, employee):
        self.employees.append(employee) 
         
    def display_employees(self):
        if not self.employees:
            print("No employees to display.")
        else:
            for employee in self.employees:
                print(employee)  

    def delete_Employee(self, emp_id):
        for e in self.employees:  
            if e.Eid == emp_id:
                self.employees.remove(e)
                print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    def update_Employee(self, emp_id):
        for e in self.employees:  
            if e.Eid == emp_id:
                print("Enter new details:")
                e.Name = input("Enter Employee Name: ")
                e.Salary = float(input("Enter Employee Salary: "))
                print("Employee updated successfully!")
        else:
            print("Employee not found.")
