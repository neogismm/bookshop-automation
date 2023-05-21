import sqlite3
import tkinter as tk
from tkinter import messagebox

con = sqlite3.connect('bookshop.db')
cursor = con.cursor()

# BOOKS table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        price REAL
    )
''')

def add_book():
    title = entry_title.get()
    author = entry_author.get()
    price = entry_price.get()

    # Insert book details into the 'books' table
    cursor.execute('INSERT INTO books (title, author, price) VALUES (?, ?, ?)', (title, author, price))
    con.commit()

    messagebox.showinfo("Success", "Book added successfully!")

def show_books():
    # Fetch all books from the 'books' table
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()

    # Display the books in a message box or any other desired way
    messagebox.showinfo("Books", str(books))

window = tk.Tk()
window.title("Bookshop Automation Software")

window.geometry("700x600")  
window.configure(bg="white")  

label_title = tk.Label(window, text="Title:")
entry_title = tk.Entry(window)

label_author = tk.Label(window, text="Author:")
entry_author = tk.Entry(window)

label_price = tk.Label(window, text="Price")
entry_price = tk.Entry(window)

button_add = tk.Button(window,text="Add Book", command=add_book)
button_show = tk.Button(window, text="Show Books", command=show_books)

label_title.pack()
entry_title.pack()
label_author.pack()
entry_author.pack()
label_price.pack()
entry_price.pack()
button_add.pack()
button_show.pack()

window.mainloop()

cursor.close()
con.close()
