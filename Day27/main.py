from tkinter import *
from tkinter.ttk import Button, Label, Entry

window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height= 300)
window.config(padx=100,pady=100)

# Creating Label
my_label = Label(text="I am a Label", font=("Arial", 20, "italic"))
# my_label.pack(side="left", expand=True)
# my_label.pack()

# Unlimited Positional Arguments
def add(*args):
    # print(type(args))
    print(args[2])
    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(3,6,4))
# print(add(5,3,3,2,5,11))

# Unlimited Keyword Arguments
def calc(n, **kwargs):
    # print(type(kwargs))
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)
calc(2, add=3, mul=5)

# Example of keyword arguments
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]   # if we use kw.get("make") then default value is set to None
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)

# Different ways of setting options
my_label.config(text="new text")
my_label["text"] = "New Text"

# Buttons
def btn_clicked():
    my_label["text"] = entry.get()

btn = Button(text="click me", command=btn_clicked)
# btn.pack()

# Entry
entry = Entry(width=30)
entry.insert(END,string="Some text")
print(entry.get())
# entry.pack()

#Text
text = Text(height=5,width=30)
text.focus()
text.insert(END,"Example of multi-line text entry.")
print(text.get("1.0",END))
# text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# Checkbutton
def checkbtn_used():
    print(checked_state.get())
checked_state = IntVar()
checkbtn = Checkbutton(text="Is On?",variable=checked_state,command=checkbtn_used)
checked_state.get()
# checkbtn.pack()

# RadioButton
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state,command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state,command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=5)
fruits = ["apple", "banana", "orange", "mango"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>",listbox_used)
# listbox.pack()

#Pack, Place and Grid
# my_label.place(x=100,y=130)
my_label.grid(column=0, row=0)
radiobutton1.grid(column=0,row=2)
btn.grid(column=1,row=1)
entry.grid(column=2,row=3)

window.mainloop()