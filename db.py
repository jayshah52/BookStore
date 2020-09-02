import sqlite3

def connect():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,  title TEXT ,author TEXT, year INTEGER, isbn integer )")
    con.commit()
    con.close()

connect()

def insert(title, author, year,isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("INSERT INTO book values(NULL, ?,?,?,?)", (title, author, year, isbn))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    con.close()
    return rows

#insert("Python", "Jay", 2020, 87778)
#insert("learn", "Khushi",2015, 968853 )
def search(title="", author="",year="" ,isbn=""):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title, author, year, isbn))
    rows = cur.fetchall()
    #con.commit()
    con.close()
    return rows

def delete(id):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id,))
    con.commit()
    con.close()

def update(id, title, author, year, isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id =?", (title, author, year, isbn, id))
    con.commit()
    con.close()

#delete(1)
#insert("Python", "Jay", 2020, 24556889)
#insert("Design", "khushi", 2019, 2441569)
print(view())
#print(search(year = 2020, author = "Khushi"))
#update(1,"JSS", "Khushi",2020, 968853 )
#print(view())
#delete(2)
#print(view())
