# #program accepting list of numbers and separate then +ve and -ve lists
# #continueex4.py
# n=int(input("Enter Values u have:")) # 5
# if(n<=0):
# 	print("{} is invalid  input".format(n))
# else:
# 	lst=list() # Create an empty list for adding dynamic list of values
# 	for i in range(1,n+1):
# 		val=int(input("Enter {} Value".format(i)))
# 		lst.append(val)
# 	else:
# 		print("------------------------------------------------------------")
# 		print("List of Values:{}".format(lst))#[-12, -34, 56, 12, -6, -4, 0, 14, 56, -78]
# 		print("------------------------------------------------------------")
# 		#Create Posstive List
# 		pslist=[] #Create an empty list for appending +ve vals
# 		for val in lst:
# 			if(val<=0):
# 				continue
# 			pslist.append(val)
# 		else:
# 			print("List of +VE Values:{}".format(pslist))#[56, 12, 14, 56]
# 			print("------------------------------------------------------------")
# 			#Create Posstive List
# 			nglist=[] #Create an empty list for appending -ve vals
# 			for val in lst:
# 				if(val>=0):
# 					continue
# 				nglist.append(val)
# 			else:
# 				print("List of -VE Values:{}".format(nglist))#[-12,-34,-6,-4,-78]
# 				print("------------------------------------------------------------")


from tkinter import *

# Function Definitions
def add():
    try:
        a = float(t1.get())
        b = float(t2.get())
        result.set(f"Addition: {a + b}")
    except ValueError:
        result.set("Error: Invalid Input!")

def subtract():
    try:
        a = float(t1.get())
        b = float(t2.get())
        result.set(f"Subtraction: {a - b}")
    except ValueError:
        result.set("Error: Invalid Input!")

def multiply():
    try:
        a = float(t1.get())
        b = float(t2.get())
        result.set(f"Multiplication: {a * b}")
    except ValueError:
        result.set("Error: Invalid Input!")

def divide():
    try:
        a = float(t1.get())
        b = float(t2.get())
        if b == 0:
            result.set("Error: Division by Zero!")
        else:
            result.set(f"Division: {a / b:.2f}")
    except ValueError:
        result.set("Error: Invalid Input!")

# Main Window
window = Tk()
window.title("Basic Calculator")
window.geometry("400x350")
window.configure(bg="#f4f4f4")

# Styling
font_style = ("Arial", 12, "bold")
btn_style = {"font": ("Arial", 10, "bold"), "width": 12, "height": 2, "bg": "#007BFF", "fg": "white"}

# Labels & Entries
Label(window, text="Enter Number 1:", font=font_style, bg="#f4f4f4").grid(row=0, column=0, pady=10, padx=10, sticky="w")
t1 = Entry(window, font=font_style)
t1.grid(row=0, column=1, padx=10)

Label(window, text="Enter Number 2:", font=font_style, bg="#f4f4f4").grid(row=1, column=0, pady=10, padx=10, sticky="w")
t2 = Entry(window, font=font_style)
t2.grid(row=1, column=1, padx=10)

# Buttons
Button(window, text="Add", command=add, **btn_style).grid(row=2, column=0, pady=10)
Button(window, text="Subtract", command=subtract, **btn_style).grid(row=2, column=1, pady=10)
Button(window, text="Multiply", command=multiply, **btn_style).grid(row=3, column=0, pady=10)
Button(window, text="Divide", command=divide, **btn_style).grid(row=3, column=1, pady=10)

# Result Label
result = StringVar()
result.set("Result will appear here")
Label(window, textvariable=result, font=font_style, fg="black", bg="#e6e6e6", width=30, height=2).grid(row=4, column=0, columnspan=2, pady=20)

# Run the Tkinter loop
window.mainloop()