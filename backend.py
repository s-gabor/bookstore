# backend.py

import sqlite3


def connection():
    conn = sqlite3.connect('books.db')
    curs = conn.cursor()
    curs.execute('CREATE TABLE IF NOT EXISTS book ("id" INTEGER PRIMARY KEY, '
                 '"title" TEXT, "author" TEXT, "year" INTEGER, "isbn" INTEGER)')
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    curs = conn.cursor()
    curs.execute('INSERT INTO book VALUES (NULL, ?, ?, ?, ?)', (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('books.db')
    curs = conn.cursor()
    curs.execute('SELECT * FROM book')
    rows = curs.fetchall()
    conn.close()
    return rows


def search(title='', author='', year='', isbn=''):
    conn = sqlite3.connect('books.db')
    curs = conn.cursor()
    curs.execute('SELECT * FROM book WHERE '
                 '"title"=? OR "author"=? OR "year"=? OR "isbn"=?', (title, author, year, isbn))
    rows = curs.fetchall()
    conn.close()
    return rows


def delete(id_):
    conn = sqlite3.connect('books.db')
    curs = conn.cursor()
    curs.execute('DELETE FROM book WHERE "id"=?', (id_,))
    conn.commit()
    conn.close()


def update(title, author, year, isbn, id_):
    conn = sqlite3.connect('books.db')
    curs = conn.cursor()
    curs.execute('UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, id_))
    conn.commit()
    conn.close()


# connection()
# insert('Morometii', 'Marin Preda', 1955, 177689758000)
# print(view())
# delete(8)
# update(6, 'Povestea lui Harap-Alb', 'Ion Creanga', 1877, 39874345654)
# print(view())
# update('100 de poeme alese', 'Mihai Eminescu', 1973, 77777, 4)
for item in view():
    print(item)
