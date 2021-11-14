from tkinter import *

window = Tk()


def miles_to_km():
    print("Inside Method", e1_text)
    print("Inside Method", e1_text.get())
    try:
        miles = float(e1_text.get())
        print("Miles == ", miles)
        km = miles * 1.63
        t1.insert(END, km)
    except Exception as e:
        print("Exception occurred", e)


b1 = Button(window, text="Execute", command=miles_to_km)
b1.grid(row=0, column=0)

e1_text = StringVar()
e1 = Entry(window, textvariable=e1_text)
e1.grid(row=0, column=2)

t1 = Text(window, height=2, width=20)
t1.grid(row=0, column=3)
window.mainloop()

# TODO Convert Miles to KM (input will have entered miles and output will show KM)

# Button method will take command param as a function and when clicked that function will be executed
# To grab the text from entry we need to pass textVariable param with StringVar()
