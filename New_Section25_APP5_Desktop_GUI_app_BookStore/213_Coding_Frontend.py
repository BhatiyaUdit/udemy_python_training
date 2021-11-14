from tkinter import *


def add_to_grid(widget, row, col, rspan=None, cspan=None):
    widget.grid(row=row, column=col, rowspan=rspan, columnspan=cspan)


window = Tk()

# Row 1
title_label = Label(master=window, text="Title")
title_entry_value = StringVar()
title_entry = Entry(master=window, textvariable=title_entry_value)
author_label = Label(master=window, text="Author")
author_entry_value = StringVar()
author_entry = Entry(master=window, textvariable=author_entry_value)

# Row 2
year_label = Label(master=window, text="Year")
year_entry_value = StringVar()
year_entry = Entry(master=window, textvariable=year_entry_value)
isbn_label = Label(master=window, text="ISBN")
isbn_entry_value = StringVar()
isbn_entry = Entry(master=window, textvariable=isbn_entry_value)

# Row 3 to End List Area
book_list_area = Listbox(master=window, height=10, width=50)
scroll_bar_books = Scrollbar(master=window)

book_list_area.configure(yscrollcommand=scroll_bar_books.set)
scroll_bar_books.configure(command=book_list_area.yview)

# Row 3 to End Buttons
view_all_btn = Button(window, text="View All", width=15)
search_btn = Button(window, text="Search Entry", width=15)
add_btn = Button(window, text="Add Entry", width=15)
update_btn = Button(window, text="Update Selected", width=15)
delete_btn = Button(window, text="Delete Selected", width=15)
close_btn = Button(window, text="Close", width=15)

add_to_grid(title_label, 0, 0)
add_to_grid(title_entry, 0, 1)
add_to_grid(author_label, 0, 2)
add_to_grid(author_entry, 0, 3)

add_to_grid(year_label, 1, 0)
add_to_grid(year_entry, 1, 1)
add_to_grid(isbn_label, 1, 2)
add_to_grid(isbn_entry, 1, 3)
add_to_grid(book_list_area, 2, 0, 6, 2)
add_to_grid(scroll_bar_books, 2, 2, 6)

# Add buttons to Grid
add_to_grid(view_all_btn, 2, 3)
add_to_grid(search_btn, 3, 3)
add_to_grid(add_btn, 4, 3)
add_to_grid(update_btn, 5, 3)
add_to_grid(delete_btn, 6, 3)
add_to_grid(close_btn, 7, 3)

window.mainloop()
