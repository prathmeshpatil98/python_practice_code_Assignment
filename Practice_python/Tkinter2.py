from tkinter import * 
from tkinter import messagebox

from regex import R

def list1to2():
    nm = list1.get(ACTIVE)
    list2.insert(END , nm)
    list1.delete(ACTIVE)
    
def list2to1():
    nm1 = list2.get(ACTIVE)
    list1.insert(END , nm1)
    list2.delete(ACTIVE)
    
    
window = Tk()

window.title(" Listw Demo Gui")
window.geometry("400x500")

frame = Frame(window)
list1 = Listbox(window)
list2 = Listbox(window)

btn1 = Button(frame , text=">>" , command=list1to2)
btn2 = Button(frame , text=">>" , command=list2to1)


btn1.pack()
btn2.pack()

list1.grid(row=1 , column=1)
frame.grid(row=1 , column=1,padx=10,pady=10)
list2.grid(row=1,column=3)


list1.insert(END , " Rohit")
list1.insert(END , " Hardik")
list1.insert(END , " Bumrah")

list2.insert(END , " Rohit")
list2.insert(END,"Ms Dhoni")


window.mainloop()
