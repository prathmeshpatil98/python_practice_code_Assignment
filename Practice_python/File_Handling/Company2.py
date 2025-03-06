# from Employee import Employee1

# class Company:
#     def _init_(self, name):
#         self.name = name

#     def addEmployee(self, id, name, sal):
#         e = Employee1(id, name, sal)
#         with open("empdata.txt", "a") as fp:
#             fp.write(str(e))

#     def displayEmployee(self):
#         try:
#             with open("employeedata.txt", "a") as fp:
#                 for line in fp:
#                     print(line.strip())
#         except FileNotFoundError:
#             print("No employee data found.")


import os
from Employee import Employee1

class Company:
    def __init__(self):
        self.filename = r"D:\\1FirstBit_Python\\python_practice_code_Assignment\\Practice_python\\File_Handling\\empdata.txt"
        folder_path = os.path.dirname(self.filename)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def addEmployee(self, employee):
        with open(self.filename, "a") as fp:
            fp.write(str(employee))  

    def displayEmployee(self):
        try:
            with open(self.filename, "r") as fp:
                for line in fp:
                    line = line.strip() 
                    data = line.split(",")
                    if len(data) == 3:
                        Eid, Name, Salary = data
                        print(f"Id: {Eid}, Name: {Name}, Salary: {Salary}")
                    else:
                        print("Invalid data found . ")
        except FileNotFoundError:
            print("No employee data found.")

    # def delete_Employee(self, id):
    #     # try:
    #         with open(self.filename, "r") as fp:
    #             employees = fp.readlines()
    #         with open(self.filename, "w") as fp:
    #             for emp in employees:
    #                 if not emp.startswith(str(id) + ","):
    #                     fp.write(emp)
    #         print("Employee deleted successfully!")
    #     # except FileNotFoundError:
    #     #     print("No employee data found.")
    
    def delete_Employee(self, id):
        employees = []

        with open(self.filename, "r") as fp:
            for emp in fp:
                split_emp = emp.strip().split(",")
                if split_emp[0] != str(id):
                    employees.append(emp)  

        with open(self.filename, "w") as fp:
            fp.writelines(employees)

        print("Employee deleted successfully!")


    # def update_Employee(self, id):
    #     try:
    #         with open(self.filename, "r") as fp:
    #             employees = fp.readlines()
    #         with open(self.filename, "w") as fp:
    #             for emp in employees:
    #                 if emp.startswith(str(id) + ","):
    #                     Name = input("Enter New Name: ")
    #                     Salary = float(input("Enter New Salary: "))
    #                     fp.write(f"{id},{Name},{Salary}\n")
    #                     print("Employee updated successfully!")
    #                 else:
    #                     fp.write(emp)
    #     except FileNotFoundError:
    #         print("No employee data found.")
