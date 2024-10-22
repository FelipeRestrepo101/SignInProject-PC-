#  if you want to view sqlite3 files, you can either use external tools on the web to open and view them, 
# or you can use this basic viewDB.py script that prints out the database records upon running.

import sqlite3 as sql
conn = sql.connect('usersDB.db')
c = conn.cursor()

c.execute('SELECT * FROM users')
rows = c.fetchall()

for row in rows:
    print(row)