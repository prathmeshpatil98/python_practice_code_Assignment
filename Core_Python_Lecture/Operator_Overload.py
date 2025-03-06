class MyTime:
    
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def display(self):
        print(f"{self.hour} : {self.minute} : {self.second} ")
        
    def __add__(self,t2):
        t3 = MyTime()
        t3.hour = self.hour + t2.hour
        t3.minute = self.minute + t2.minute
        t3.second = self.second + t2.second
        return t3
    
    def __sub__(self,t2):
        t3 = MyTime()
        t3.hour = self.hour + t2.hour
        t3.minute = self.minute + t2.minute
        t3.second = self.second + t2.second
        return t3
    

t1 = MyTime(10,20,30)
t1.display()

t2 = MyTime(5,6,7)
t2.display()

t3 = t2 + t1 
t3.display()

t4 = t1 - t2 
t3.display()