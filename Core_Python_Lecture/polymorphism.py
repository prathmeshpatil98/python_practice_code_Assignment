class Vehicle:
    
    count = 0
    
    def __init__(self, com, model, price, color):
        self.company = com
        self.model = model
        self.__price = price
        self.color = color
        Vehicle.count += 1
        
    def Display(self):
        print("Company =", self.company)
        print("Model =", self.model)
        print("Price =", self.__price)
        print("Color =", self.color)
        
    def Brake(self):
        print("Brake is applied.")
        
    def getprice(self):
        return self.__price

    def setprice(self, price):
        self.__price = price
        
    def getcount():
        # return Vehicle.count
        print(Vehicle.count)


class Car(Vehicle):
    def __init__(self, com, model, price, color, noa):
        super().__init__(com, model, price, color)
        self.airbagCount = noa
        
    def Display(self):
        super().Display()
        print("AirbagCount =", self.airbagCount)
        
    def Brake(self):
        print("ABS brake is applied.")
        
class Bike(Vehicle):
    def __init__(self, com, model, price, color, noh):
        super().__init__(com, model, price, color)
        self.helmetCount = noh
        
    def Display(self):
        super().Display()
        print("No of helmets =", self.helmetCount)
        
    def Brake(self):
        print("Disc brake is applied.")
        

veh = Vehicle('TATA', 'ABC', 9, "black")
cr = Car("Mahindra", 'ScorpioN', 16, 'white', 4)
bk = Bike("Hero", "Splendor", 1, 'silver', 2)


print(Vehicle.getcount())


# all_veh = [veh, cr, bk]

# for vehicle in all_veh:
#     vehicle.Display()
#     vehicle.Brake()
#     print()
