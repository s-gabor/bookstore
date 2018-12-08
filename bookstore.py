from tkinter import *

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

# side widgets
view_all = Button(window, text='View All', width=15)
view_all.grid(rowspan=2, column=3)

search_entry = Button(window, text='Search Entry', width=15)
search_entry.grid(row=4, column=3)


add_entry = Button(window, text='Add Entry', width=15)
add_entry.grid(row=5, column=3)


update_button = Button(window, text='Update', width=15)
update_button.grid(row=6, column=3)


delete_button = Button(window, text='Delete', width=15)
delete_button.grid(row=7, column=3)

close_button = Button(window, text='Close', width=15)
close_button.grid(row=8, column=3)


window.mainloop()
