from tkinter import *


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=30,pady=30)

entry = Entry(width=8)
entry.insert(END,string="0")
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)

answer_label = Label(text="0")
answer_label.grid(column=1,row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

def calculate_km():
    miles = float(entry.get())
    km = round(miles * 1.609)
    answer_label.config(text=f"{km}")
calc_btn = Button(text="Calculate",command=calculate_km)
calc_btn.grid(column=1,row=2)
window.mainloop()