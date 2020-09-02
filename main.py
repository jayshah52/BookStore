from tkinter import *
import db

window = Tk()

window.wm_title("Book Database")

def get_row(event):
    try:
        global selected_row
        index = list1.curselection()[0]
        #print(index)
        selected_row = list1.get(index)
        #print(selected_row[0])
        title_entry.delete(0, END)
        title_entry.insert(END,selected_row[1])
        author_entry.delete(0,END)
        author_entry.insert(END,selected_row[2])
        year_entry.delete(0, END)
        year_entry.insert(END, selected_row[3])
        isbn_entry.delete(0, END)
        isbn_entry.insert(END, selected_row[4])
    except IndexError:
        pass

def viewall():
    list1.delete(0, END)
    for row in db.view():
        list1.insert(END, row)

def search_entry():
    list1.delete(0, END)
    for row in db.search(title_val.get(), author_val.get(), year_val.get(), isbn_val.get()):
        list1.insert(END,row)

def add():
    db.insert(title_val.get(), author_val.get(), year_val.get(), isbn_val.get())
    list1.delete(0, END)
    list1.insert(END, (title_val.get(), author_val.get(), year_val.get(), isbn_val.get()))


def delete_entry():
    db.delete(selected_row[0])


def update_entry():
    db.update(selected_row[0], title_val.get(), author_val.get(), year_val.get(), isbn_val.get())



title = Label(window, text = "Title")
title.grid(row = 0, column = 0)
title_val = StringVar()
title_entry = Entry(window, textvariable = title_val)
title_entry.grid(row = 0, column = 1)

author = Label(window, text = "Author")
author.grid(row = 0, column = 2)
author_val = StringVar()
author_entry = Entry(window, textvariable = author_val)
author_entry.grid(row = 0, column = 3)

year = Label(window, text = "Year")
year.grid(row = 1, column = 0)
year_val = StringVar()
year_entry = Entry(window, textvariable = year_val)
year_entry.grid(row = 1, column = 1)

isbn = Label(window, text = "ISBN")
isbn.grid(row = 1, column = 2)
isbn_val = StringVar()
isbn_entry = Entry(window, textvariable = isbn_val)
isbn_entry.grid(row = 1, column = 3)

list1 = Listbox(window, height= 7, width = 35)
list1.grid(row =2, column= 0,rowspan = 6, columnspan = 2)

scroll = Scrollbar(window)
scroll.grid(row = 2, column = 2, rowspan = 6, columnspan = 1)

list1.configure(yscrollcommand = scroll.set)
scroll.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', get_row)

viewBtn = Button(window, text= "View All", width = 12, command = viewall)
viewBtn.grid(row = 2 ,column = 3)

searchBtn = Button(window, text= "Search Entry", width = 12, command = search_entry)
searchBtn.grid(row = 3,column = 3)

addBtn = Button(window, text= "Add Entry", width = 12, command = add)
addBtn.grid(row = 4,column = 3)

updateBtn = Button(window, text= "Update Entry", width = 12, command = update_entry)
updateBtn.grid(row = 5,column = 3)

delBtn = Button(window, text= "Delete Entry",width = 12, command = delete_entry)
delBtn.grid(row = 6,column = 3)

closeBtn = Button(window, text= "Close", width = 12, command = window.destroy)
closeBtn.grid(row = 7, column = 3)

window.mainloop()