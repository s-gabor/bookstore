# bookstore.py

from tkinter import *
from backend import Database


class Bookstore:

    def __init__(self, win):
        self.win = win
        self.db = Database('books.db')
        self.selected_row = None
        self.input_texts = []
        self.input_boxes = []

    def create_widget(self, text, row, column):
        label = Label(self.win, text=text)
        label.grid(row=row, column=column)
        text = StringVar()
        box = Entry(self.win, textvariable=text)
        box.grid(row=row, column=column+1)
        self.input_texts.append(text)
        self.input_boxes.append(box)

    def create_display(self, row, column, rowspan, columnspan):
        listbox = Listbox(self.win, height=6, width=30)
        listbox.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
        sb = Scrollbar(self.win)
        sb.grid(row=row, column=(column+columnspan), rowspan=rowspan)
        listbox.configure(yscrollcommand=sb.set)
        sb.configure(command=listbox.yview)
        listbox.bind('<<ListboxSelect>>', self.get_selected_row)
        self.lb = listbox

    def create_button(self, label, width, command, row, column):
        button = Button(self.win, text=label, width=width, command=command)
        button.grid(row=row, column=column)

    def get_selected_row(self, event):
        try:
            row_number = self.lb.curselection()[0]
            self.selected_row = self.lb.get(row_number)
            for data, entry in zip((self.selected_row[1], self.selected_row[2], self.selected_row[3], self.selected_row[4]),
                                   (self.input_boxes[0], self.input_boxes[1], self.input_boxes[2], self.input_boxes[3])):
                entry.delete(0, END)
                entry.insert(END, data)
        except IndexError as e:
            print('It looks like no selection was made. The following exception was silenced:\n', e)
            self.lb.insert(END, 'Please select a valid entry!')

    def view_command(self):
        self.lb.delete(0, END)
        for item in self.db.view():
            self.lb.insert(END, item)

    def search_command(self):
        self.lb.delete(0, END)
        for item in self.db.search(self.input_texts[0].get(), self.input_texts[1].get(), self.input_texts[2].get(), self.input_texts[3].get()):
            self.lb.insert(END, item)

    def add_command(self):
        self.db.insert(self.input_texts[0].get(), self.input_texts[1].get(), self.input_texts[2].get(), self.input_texts[3].get())
        self.lb.delete(0, END)
        data = self.db.search(self.input_texts[0].get(), self.input_texts[1].get(), self.input_texts[2].get(), self.input_texts[3].get())
        print(data)
        for item in data:
            self.lb.insert(END, item)
        for entry in self.input_boxes:
            entry.delete(0, END)
        self.view_command()

    def update_command(self):
        self.db.update(self.input_texts[0].get(), self.input_texts[1].get(), self.input_texts[2].get(), self.input_texts[3].get(), self.selected_row[0])
        self.view_command()

    def delete_command(self):
        self.db.delete(self.selected_row[0])
        self.view_command()

    def close_command(self):
        self.win.destroy()


window = Tk()

books = Bookstore(window)

books.create_widget('Title', 0, 0)
books.create_widget('Author', 0, 2)
books.create_widget('Year', 1, 0)
books.create_widget('ISBN', 1, 2)

books.create_display(2, 0, 6, 2)

books.create_button('View all', 15, books.view_command, 2, 3)
books.create_button('Search', 15, books.search_command, 3, 3)
books.create_button('Add entry', 15, books.add_command, 4, 3)
books.create_button('Update', 15, books.update_command, 5, 3)
books.create_button('Delete', 15, books.delete_command, 6, 3)
books.create_button('Close', 15, books.close_command, 7, 3)

window.mainloop()

# ('Ion', 'Liviu Rebreanu', 1954, 111)
# ('Enigma Otiliei', 'George Calinescu', 1938, 222)
# ('Toate panzele sus!', 'Radu Tudoran', 1954, 333)
# ('100 de poeme alese', 'Mihai Eminescu', 1973, 444)
# ('Povestea lui Harap-Alb', 'Ion Creanga', 1877, 666)
# ('Morometii', 'Marin Preda', 1955, 777)
# ('O scrisoare pierduta', 'I. L. Caragiale', 1884, 888)
