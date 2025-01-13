# program to covert days into years, week, days

day=int(input("Enter number of days: "))
years=day//365
day=day%365
weeks=day//7
day=day%7

print(f"The year , weeks, days are {  years}, {weeks}, {day}")