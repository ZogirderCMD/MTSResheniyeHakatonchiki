import sqlite3 as sq
import random

con = sq.connect("database.db")

cur = con.cursor()
cur.execute("""SELECT * FROM users""")
for i in range(len(cur.fetchall())):
    cur.execute(f"""UPDATE users SET age = {random.randint(18, 40)} WHERE rowid = {i}""")

con.commit()
