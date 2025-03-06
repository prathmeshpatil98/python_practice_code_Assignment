class Employee:
    def __init__(self,eid,name,salary):
        self.eid=eid
        self.name= name
        self.salary = salary
    
    def __str__(self):
         return str(self.eid)+","+self.name+","+str(self.salary)
    