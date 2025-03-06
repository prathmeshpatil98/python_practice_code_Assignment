from tkinter import *


def add():
    a = int(t1.get())
    b = int(t1.get())
    c = a + b 
    l3.config(text=" Addition is : "+ str(c))
    l1.config()

def mult():
    a = int(t1.get())
    b = int(t2.get())
    c = a * b 
    l4.config(text=" Multiplication is : "+ str(c)) 
    l1.config()
    
def Div():
    a = int(t1.get())
    b = int(t2.get())
    c = a // b 
    l5.config(text=" Division  is : "+ str(c)) 
    l1.config()
    
def substract():
    a = int(t1.get())
    b = int(t2.get())
    c = a - b 
    l6.config(text=" Subtract  is : "+ str(c)) 
    l1.config()

window = Tk()

window.title("Demo GUI Addition.")
window.geometry("400x300")
window.configure(bg="#f4f4f4")

l1 = Label(window,text="Enter Number 1 : ")
l2 = Label(window,text="Enter Number 2 : ")
l3 = Label(window,text=" ")
l4 = Label(window,text=" ")
l5 = Label(window,text=" ")
l6 = Label(window,text=" ")
t1 = Entry(window)
t2 = Entry(window)

button1 = Button(window,text="Add", command= add)
button2 = Button(window,text="Multiply", command= mult)
button3 = Button(window,text="Division", command= Div )
button4 = Button(window,text="Subtrac",command=substract)


    
l1.grid(row=1 , column=1 )
t1.grid(row=1 , column=2 )
l2.grid(row=2 , column=1 )
t2.grid(row=2 , column=2 )
button1.grid(row=3 , column=1 )
l3.grid(row = 4 , column = 2)
button2.grid(row=3 , column=2 )
l4.grid(row = 4 , column = 2)
button3.grid(row=3,column=3)
l5.grid(row=4 , column=2)
button4.grid(row=3,column=4)
l5.grid(row=4 , column=2)



window.mainloop()