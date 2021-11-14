from tkinter import *

window = Tk()

button = Button(master=window, text="Hello Button")
# button.pack()

button.grid(row=1, column=1, rowspan=5)
entry = Entry(window)
entry.grid(row=0, column=0, rowspan=2)

textt = Text(window, height=1, width=30)
textt.grid(row=1, column=2)

window.mainloop()

#
# Basic Minimum needed to create a window :
# window = Tk()
# window.mainloop()
#
# Once we have window we can add widgets like button, inputs , etc
#   To add button we need to use Button() method : check the params before usage
#       button = Button(master=window, text="Hello Button")
#       button.pack()
#
#       We can also use grid method to show button
#       Grid is used because it give more control over the positions of the widgets
#
#       Entry is a widget that allow us to input values in the window
#       To show some details we can use Text widget that can show value on screen
#           Default height and width is too large change while creating
#           #######
