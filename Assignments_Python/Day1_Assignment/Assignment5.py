# program to enter p, t, r and calculate compound interest

p=int(input("Enter principle amount : "))
r=int(input("Enter rate of interest : "))
t=int(input("Enter time period in year : "))

total=p*(1+r)**t
ci=total-p

print(f"The compound interest is {ci}")