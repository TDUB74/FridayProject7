import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to create the SQLite database and table
def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 email TEXT UNIQUE,
                 password TEXT)''')
    conn.commit()
    conn.close()

# Function to insert user data into the database
def insert_user(email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''INSERT INTO users (email, password)
                 VALUES (?, ?)''', (email, password))
    conn.commit()
    conn.close()

# Function to validate email format
def validate_email(email):
    return "@" in email and "." in email[email.find("@"):]

# Function to validate password
def validate_password(password1, password2):
    return password1 == password2

# Function to handle sign up button click
def sign_up():
    email = email_entry.get()
    password1 = password_entry.get()
    password2 = confirm_password_entry.get()

    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format")
    elif not validate_password(password1, password2):
        messagebox.showerror("Error", "Passwords do not match")
    else:
        insert_user(email, password1)
        messagebox.showinfo("Success", "Account created successfully")

# Main window for sign up
def sign_up_window():
    global email_entry, password_entry, confirm_password_entry

    window = tk.Tk()
    window.title("Sign Up")

    tk.Label(window, text="Email:").pack()
    email_entry = tk.Entry(window)
    email_entry.pack()

    tk.Label(window, text="Password:").pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    tk.Label(window, text="Confirm Password:").pack()
    confirm_password_entry = tk.Entry(window, show="*")
    confirm_password_entry.pack()

    tk.Button(window, text="Sign Up", command=sign_up).pack()

    window.mainloop()

# Main function
if __name__ == "__main__":
    create_table()
    sign_up_window()
