# Convert the time entered in hh,min and sec into seconds.

hour = int(input("Please Enter the hour : "))

minute = int(input("Please Enter the minute : "))

second = int(input("Please Enter the second : "))   

total_second = hour * 3600 + minute * 60 + second

print(f"The total second is {total_second}")

