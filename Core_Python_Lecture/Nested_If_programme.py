option=0
while(option != 4):

    print("1 . Area of Circle")
    print("2 . profit Calculation")
    print("3 . Number is positive or Negative")
    print("4 . Exit ")

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
    elif(option == 4):
        break
    else:
        print("Please Enter the Valid Option .")