# backend.py

import sqlite3


class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.curs = self.conn.cursor()
        self.curs.execute('CREATE TABLE IF NOT EXISTS book ("id" INTEGER PRIMARY KEY, '
                          '"title" TEXT, "author" TEXT, "year" INTEGER, "isbn" INTEGER)')
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.curs.execute('INSERT INTO book VALUES (NULL, ?, ?, ?, ?)', (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.curs.execute('SELECT * FROM book')
        rows = self.curs.fetchall()
        return rows

    def search(self, title='', author='', year='', isbn=''):
        self.curs.execute('SELECT * FROM book WHERE '
                          '"title"=? OR "author"=? OR "year"=? OR "isbn"=?', (title, author, year, isbn))
        rows = self.curs.fetchall()
        return rows

    def delete(self, id_):
        self.curs.execute('DELETE FROM book WHERE "id"=?', (id_,))
        self.conn.commit()

    def update(self, title, author, year, isbn, id_):
        self.curs.execute('UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?',
                          (title, author, year, isbn, id_))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        print('db closed')
