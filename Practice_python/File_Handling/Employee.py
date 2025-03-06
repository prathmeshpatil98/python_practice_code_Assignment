class Employee1:
    def __init__(self, Eid=0, Name='', Salary=0.0):
        self.Eid = Eid
        self.Name = Name
        self.Salary = Salary

    def __str__(self):
        return f"{self.Eid},{self.Name},{self.Salary}\n"

