from tkinter import *
import tkinter.messagebox

def calculate():
    ent1 = entry1.get()
    ent2 = entry2.get()
    var_cal = var.get()
    if ent1.isdigit() == True and ent2.isdigit() == True:
        if var_cal == "1":
            result = int(ent1) + int(ent2)
            tkinter.messagebox.showinfo("Result", result)
        elif var_cal == "2":
            result = int(ent1) - int(ent2)
            tkinter.messagebox.showinfo("Result", result)
        elif var_cal == "3":
            if int(ent1) == 0 or int(ent2) == 0:
                tkinter.messagebox.showinfo("Result", "0")
            else:
                result = int(ent1) * int(ent2)
                tkinter.messagebox.showinfo("Result", result)
        elif var_cal == "4":
            if int(ent2) == 0:
                tkinter.messagebox.showinfo("Ops!", "You can't divide by 0")
            else:
                result = int(ent1) / int(ent2)
                tkinter.messagebox.showinfo("Result", result)      
    else:
        tkinter.messagebox.showinfo("Ops!", "Digits only")
        if ent1.isdigit() != True:
            entry1.focus_set()
        elif ent2.isdigit() != True:
            entry2.focus_set()
        
    

root = Tk()
root.title("Simple calculator")
var = StringVar()
var.set("1")


# create widgets
entry1 = Entry(root, width=10)
entry2 = Entry(root, width=10)
button = Button(root, text="Calculate", command=calculate)
addition = Radiobutton(root, text="+", variable = var, value="1", padx=20)
subtraction = Radiobutton(root, text="-", variable = var, value="2", padx=20)
multiplication = Radiobutton(root, text="*", variable = var, value="3", padx=20)
division = Radiobutton(root, text="/", variable = var, value="4", padx=20)


# add widgets to main window
entry1.grid(rowspan=4)
addition.grid(row=0, column=1)
subtraction.grid(row=1, column=1)
multiplication.grid(row=2, column=1)
division.grid(row=3, column=1)
entry2.grid(row=0, column=2, rowspan=4)
button.grid(row=4, columnspan=3)


root.mainloop()
