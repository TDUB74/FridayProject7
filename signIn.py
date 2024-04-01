import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to check if the email/password combination exists in the database
def check_credentials(email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM users WHERE email=? AND password=?''', (email, password))
    result = c.fetchone()
    conn.close()
    return result is not None

# Function to handle sign in button click
def sign_in():
    email = email_entry.get()
    password = password_entry.get()

    if check_credentials(email, password):
        messagebox.showinfo("Success", "Log in successful", icon="info")
    else:
        messagebox.showerror("Error", "Email or password incorrect")

# Main window for sign in
def sign_in_window():
    global email_entry, password_entry

    window = tk.Tk()
    window.title("Sign In")

    tk.Label(window, text="Email:").pack()
    email_entry = tk.Entry(window)
    email_entry.pack()

    tk.Label(window, text="Password:").pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    tk.Button(window, text="Sign In", command=sign_in).pack()

    window.mainloop()

if __name__ == "__main__":
    sign_in_window()

