from Employee import Employee

class Company:
    def __init__(self,name):
        self.name=name
        self.employees =[]
    
    def addEmployee(self,id,nm,sal):
        e= Employee(id,nm,sal)
        self.employees.append(e)
    
    def displayEmployee(self):

        for e in self.employees:
            print(e)
            
    def displayEmployee(self,)