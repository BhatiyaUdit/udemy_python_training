from tkinter import *

window = Tk()


def convert_KG():
    print("Conversion Started", ip_var.get())
    try:
        kilo_gram = float(ip_var.get())
        gram = kilo_gram * 1000
        t1.insert(END, gram)

        pounds = kilo_gram * 2.20462
        t2.insert(END, pounds)

        ounces = kilo_gram * 35.274
        t3.insert(END, ounces)

    except Exception as e:
        print("Execption occurred", e)


static_text = Label(window, text="Kg")
static_text.grid(row=0, column=0)

ip_var = StringVar()
input_text = Entry(window, textvariable=ip_var)
input_text.grid(row=0, column=1)

convert_btn = Button(window, text="Convert", command=convert_KG)
convert_btn.grid(row=0, column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

l1 = Label(window, text="Gram")
l1.grid(row=2, column=0)

l2 = Label(window, text="Pound")
l2.grid(row=2, column=1)

l3 = Label(window, text="Ounces")
l3.grid(row=2, column=2)

window.mainloop()


# TODO :   # Empty the Text boxes if they had text from the previous use and fill them again
#     t1.delete("1.0", END)  # Deletes the content of the Text box from start to END
