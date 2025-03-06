from Company2 import Company
from Employee import Employee1

company = Company()

while True:
    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Delete Employee")
    print("4. Update Employee")
    print("10. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        print("\nEnter Employee Details:")
        Eid = int(input("Enter Employee Id: "))
        Name = input("Enter Employee Name: ")
        Salary = float(input("Enter Employee Salary: "))

        employee = Employee1(Eid, Name, Salary)
        company.addEmployee(employee)
        print("Employee added successfully!")

    elif ch == 2:
        print("\nEmployee List:")
        company.displayEmployee()

    elif ch == 3:
        id = int(input("Please Enter the Id: "))
        company.delete_Employee(id)

    elif ch == 4:
        id = int(input("Please Enter the Id: "))
        company.update_Employee(id)

    elif ch == 10:
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please enter a valid option.")