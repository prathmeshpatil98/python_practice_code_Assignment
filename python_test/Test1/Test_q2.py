#2 write a programme to calculate Simple interest 

principle = int(input("Please Enter the Principle : "))
rate = int(input("Please Enter the Rate : "))
Time = int(input("Please Enter the time : "))

simple_interest = (principle * rate * Time ) / 100


print("The simple Interest is ", simple_interest)
