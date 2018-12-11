# bookstore.py

import backend
from tkinter import *


def get_selected_row(event):
    try:
        row_number = display_area.curselection()[0]
        global selected_tuple
        selected_tuple = display_area.get(row_number)
        for data, entry in zip((selected_tuple[1], selected_tuple[2], selected_tuple[3], selected_tuple[4]),
                               (title_box, author_box, year_box, isbn_box)):
            entry.delete(0, END)
            entry.insert(END, data)
    except IndexError as e:
        print('It looks like no selection was made. Exception was silenced: ', e)
        display_area.insert(END, e)


def view_command():
    display_area.delete(0, END)
    for item in backend.view():
        display_area.insert(END, item)


def search_command():
    display_area.delete(0, END)
    for item in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        display_area.insert(END, item)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    display_area.delete(0, END)
    for item in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        display_area.insert(END, item)
    for entry in [title_box, author_box, year_box, isbn_box]:
        entry.delete(0, END)


def update_command():
    backend.update(title_text.get(), author_text.get(), year_text.get(), isbn_text.get(), selected_tuple[0])
    view_command()


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()


def close_command():
    window.destroy()


window = Tk()

title_label = Label(window, text='Title')
author_label = Label(window, text='Author')
year_label = Label(window, text='Year')
ISBN_label = Label(window, text='ISBN')
title_label.grid(row=0, column=0)
author_label.grid(row=0, column=2)
year_label.grid(row=1, column=0)
ISBN_label.grid(row=1, column=2)

title_text = StringVar()
title_box = Entry(window, textvariable=title_text)
title_box.grid(row=0, column=1)

author_text = StringVar()
author_box = Entry(window, textvariable=author_text)
author_box.grid(row=0, column=3)

year_text = StringVar()
year_box = Entry(window, textvariable=year_text)
year_box.grid(row=1, column=1)

isbn_text = StringVar()
isbn_box = Entry(window, textvariable=isbn_text)
isbn_box.grid(row=1, column=3)

display_area = Listbox(window, height=6, width=30)
display_area.grid(row=3, column=0, rowspan=6, columnspan=2)
sb = Scrollbar(window)
sb.grid(row=3, column=2, rowspan=6)
display_area.configure(yscrollcommand=sb.set)
sb.configure(command=display_area.yview)

display_area.bind('<<ListboxSelect>>', get_selected_row)

# side widgets
view_all = Button(window, text='View All', width=15, command=view_command)
view_all.grid(row=2, column=3, rowspan=2)


search_entry = Button(window, text='Search Entry', width=15, command=search_command)
search_entry.grid(row=4, column=3)


add_entry = Button(window, text='Add Entry', width=15, command=add_command)
add_entry.grid(row=5, column=3)


update_button = Button(window, text='Update', width=15, command=update_command)
update_button.grid(row=6, column=3)


delete_button = Button(window, text='Delete', width=15, command=delete_command)
delete_button.grid(row=7, column=3)

close_button = Button(window, text='Close', width=15, command=close_command)
close_button.grid(row=8, column=3)


window.mainloop()

# ('Ion', 'Liviu Rebreanu', 1954, 111)
# ('Enigma Otiliei', 'George Calinescu', 1938, 222)
# ('Toate panzele sus!', 'Radu Tudoran', 1954, 333)
# ('100 de poeme alese', 'Mihai Eminescu', 1973, 444)
# ('Povestea lui Harap-Alb', 'Ion Creanga', 1877, 666)
# ('Morometii', 'Marin Preda', 1955, 777)
# ('O scrisoare pierduta', 'I. L. Caragiale', 1884, 888)
