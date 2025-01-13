# write a program to enter p, t, r and calculate simple interest

p= int(input("Enter principle amount : "))
r= int(input("Enter rate of interest : "))
t= int(input("Enter time period in year : "))

total= p*r*t
si= total/100

print(f"The simple interest of amount {p} for {t} time at {r} is {si}")