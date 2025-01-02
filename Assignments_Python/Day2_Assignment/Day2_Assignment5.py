 #WAP to calculate selling price of book based on cost price and discount. 
 
cost_price = int(input("Please Enter the cost price : "))
discount = int(input("Please Enter the discount : "))

selling_price = cost_price - (cost_price * discount)/100

print(f"The selling price is {selling_price}")

