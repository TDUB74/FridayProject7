

This is a simple user portal application implemented in Python using Tkinter for the GUI and SQLite for the database. It consists of two main functionalities: sign-up and sign-in.



- `sign_up.py`: Contains the code for the sign-up functionality. Users can enter their email and password to create an account. The email is validated to ensure it follows a valid format, and the password is verified by requiring the user to enter it twice.
  
- `sign_in.py`: Contains the code for the sign-in functionality. Registered users can log in to their account using their email and password. If the email/password combination exists in the database, a message in green is displayed indicating successful login. Otherwise, a message in red is displayed indicating incorrect email or password.

- `users.db`: SQLite database file where user information (email and password) is stored.



To run the application, execute `sign_up.py` for the sign-up window and `sign_in.py` for the sign-in window. Both windows interact with the same SQLite database (`users.db`).



- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- SQLite (comes pre-installed with Python)



1. Install Python 3.x if not already installed.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the files.
4. Run `python sign_up.py` to open the sign-up window.
5. Run `python sign_in.py` to open the sign-in window.



Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.


