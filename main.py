from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles*1.609
    kilometer_result_label.config(text=f"{km}")

window= Tk()
window.title("Mile to Km Converter")
window.minsize(width=100,height=100)
window.config(padx=20,pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=4,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=5,row=0)
miles_label.config(padx=20,pady=20)

is_equal_lable=Label(text="is equal to")
is_equal_lable.grid(column=3,row=1)
is_equal_lable.config(padx=10,pady=10)

kilometer_result_label =Label(text="0")
kilometer_result_label.grid(column=4,row=1)
kilometer_result_label.config(padx=10,pady=10)

kilometer_label =Label(text="Km")
kilometer_label.grid(column=5,row=1)
kilometer_label.config(padx=10,pady=10)

calculate_button=Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=4,row=3)

window.mainloop()