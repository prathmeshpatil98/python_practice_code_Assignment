class Employee():
    def __init__(self,id,name,sallary):
        self.id = id
        self.name = name 
        self.sallary = sallary
        
        
    def display(self):
        print(f"ID =  {self.id}")
        print(f"ID =  {self.name}")
        print(f"ID =  {self.sallary}")
        

class Admin(Employee):
    def __init__(self, id, name, sallary,allowance):
        super().__init__(id, name, sallary)
        self.allowance = allowance
        
    def display(self):
        super().display()
        print(f"Allowance = {self.allowance}")
        
emp = Employee(1,"prathamesh",60000)
emp.display()
print("----------------------------------------")
adm = Admin(2,"Angha",45000,2000)
adm.display()
    