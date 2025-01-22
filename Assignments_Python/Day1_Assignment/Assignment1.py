# calculate percentage of student based on marks
id = int(input("Please Enter the Id : "))
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: "))
sub5 = int(input("Enter marks of subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total/5

print("Total percentage is the {0}".format(percentage))
print(f"Total percentage is the {id} = {percentage}")
