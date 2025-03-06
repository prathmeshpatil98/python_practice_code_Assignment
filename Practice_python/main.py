from company import Company


c = Company("FBS")

ch=0
while(ch!=10):
    print("1.Add employee")
    print("2. Didplsy all employees")
    print("10.Exit")
    ch = int(input("Enter choice: "))

    if(ch==1):
        id = int(input("Enter id: "))
        nm = input("Enter name:")
        sal = int(input("Enter salary: "))
        c.addEmployee(id,nm,sal)
    elif(ch==2):
        c.displayEmployee()