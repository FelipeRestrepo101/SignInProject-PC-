import tkinter as tk
import datetime
import sqlite3 as sql


def get_input():
    user_input_Name = entry_label_Name.get()
    user_input_Email = entry_label_Email.get()

    # start of db code

    #upon clicking the  'sign in' button this script will now create the database file 'usersDB.db' in the same directory you have your .py script, 
    #if the database doesn't already exist. Otherwise it will access the existing 'usersDB.db' file, and insert the sign in entry as a new record. 
    conn = sql.connect('usersDB.db')
    c = conn.cursor()


    c.execute('''
            CREATE TABLE IF NOT EXISTS users
            (name STRING, age INT, date STRING)
              ''')
    
    c.execute('''
            INSERT INTO users (name, age, date) VALUES (?, ?, ?)
              ''', (user_input_Name, user_input_Email, str(datetime.date.today()))
             )
    
    conn.commit()
    # end of db code
    

    entry_label_Name.delete(0, tk.END)  # Clear the entry field
    entry_label_Email.delete(0, tk.END)  

window = tk.Tk()
window.title("Sign In Sheet")
window.geometry("600x400")

label_Name = tk.Label(window, text="Enter Your Name:")
label_Name.pack()
#label_Name.grid(row=0, column=0)

entry_label_Name = tk.Entry(window)
entry_label_Name.pack()
#entry_label_Name.grid(row=0, column=1)

label_Email = tk.Label(window, text="Enter Your Student Email:")
label_Email.pack()

entry_label_Email = tk.Entry(window)
entry_label_Email.pack()

button = tk.Button(window, text="Sign in", command=get_input)
button.pack()

window.mainloop()
