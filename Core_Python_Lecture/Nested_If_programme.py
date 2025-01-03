print("1 . Area of Circle")
print("2 . profit Calculation")
print("3 . Number is positive or Negative")

option = int(input("Please Enter the Option You want : "))

if(option == 1):
    radius = int(input("please Enter the Number :"))
    area = 3.14 * radius * radius
    print(area ,"Is the Area of Circle") 
elif(option == 2):
    Selling_Price = int(input("Please Enter the Selling Price :"))
    cost_price = int(input("please Enter the cost Price : "))
    if(Selling_Price > cost_price):
        profit = Selling_Price - cost_price
        print(profit , " Rs , This is the Profit")
    else:
        print("you have Loss")
elif(option == 3 ):
    number = int(input("Please Enter the Number"))
    if(number < 0):
        print(number,"This is the Positive Number")
    elif(number > 0):
        print(number,"This is the Negative Number")
    else:
        print(number,"This is Neutral")
else:
    print("Please Enter the number between 1 to 3 ")