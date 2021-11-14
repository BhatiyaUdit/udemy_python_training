from tkinter import *
from backend import *


def add_to_grid(widget, row, col, rspan=None, cspan=None):
    widget.grid(row=row, column=col, rowspan=rspan, columnspan=cspan)


def view_command():
    book_list_area.delete(0, END)
    data = view_all()
    print(data)
    for row in data:
        book_list_area.insert(END, row)


def search_command():
    book_list_area.delete(0, END)
    data = search(author=author_entry_value.get(),
                  title=title_entry_value.get(),
                  year=year_entry_value.get(),
                  isbn=isbn_entry_value.get())
    for row in data:
        book_list_area.insert(END, row)


def insert_command():
    book_list_area.delete(0, END)
    insert_book(title=title_entry_value.get(),
                author=author_entry_value.get(),
                year=year_entry_value.get(),
                isbn=isbn_entry_value.get())

    book_list_area.insert(END, "Record inserted Click On View All to check")
    title_entry_value.set("")
    author_entry_value.set("")
    year_entry_value.set("")
    isbn_entry_value.set("")
    # TODO : Check empty insertion


def update_command():
    print(row_selected)
    update(row_selected[0]
           , title=title_entry_value.get()
           , author=author_entry_value.get()
           , year=year_entry_value.get()
           , isbn=isbn_entry_value.get())
    view_command()


def delete_command():
    print(row_selected)
    delete(row_selected[0])
    view_command()


def row_selection_handler(event):
    global row_selected
    if book_list_area.curselection():
        row_selected_index = book_list_area.curselection()[0]
        row_selected = book_list_area.get(row_selected_index)

        # Clear Entry cell on selection
        title_entry.delete(0, END)
        author_entry.delete(0, END)
        year_entry.delete(0, END)
        isbn_entry.delete(0, END)

        # Fill Entry Cell with selected Data
        title_entry.insert(END, row_selected[1])
        author_entry.insert(END, row_selected[2])
        year_entry.insert(END, row_selected[3])
        isbn_entry.insert(END, row_selected[4])
    else:
        print("Nothing present in the box")


window = Tk()

window.wm_title("Udit Book Store")
connect()

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

book_list_area.bind('<<ListboxSelect>>', row_selection_handler)

# Row 3 to End Buttons
view_all_btn = Button(window, text="View All", width=15, command=view_command)
search_btn = Button(window, text="Search Entry", width=15, command=search_command)
add_btn = Button(window, text="Add Entry", width=15, command=insert_command)
update_btn = Button(window, text="Update Selected", width=15, command=update_command)
delete_btn = Button(window, text="Delete Selected", width=15, command=delete_command)
close_btn = Button(window, text="Close", width=15, command=window.destroy)

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

# To Fill the cell in case of selected Row we need to use Bind Method , just for deletion it is not needed
