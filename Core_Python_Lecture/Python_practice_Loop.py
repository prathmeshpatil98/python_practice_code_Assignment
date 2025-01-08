Passengers=int(input("Please Enter the number of Passengers : "))
ticket_price = float(input("Enter the ticket price : "))

total_amount = 0

for i in range(1 , Passengers+1):
    age = int(input("Please Enter the Age : "))
    if age <= 12:
        total_amount += ticket_price * 0.70 
    elif age >= 59:
        total_amount += ticket_price * 0.50  
    else:
        total_amount += ticket_price 
        

print("The Total Price is of the Ticket is  ",total_amount)