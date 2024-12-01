import pandas as pd
import sqlite3 as sq

con = sq.connect("database.db")
cur = con.cursor()

df = pd.read_csv("a.csv")

txt1 = "("
for i in df:
    txt1 += f"'{i}',"
txt1 += ")"
txt1 = txt1[:len(txt1)-2]+")"

for i in range(len(df)):
    txt2 = "("
    for j in range(len(df.iloc[i])):
        txt2 += f"'{df.iloc[i][j]}',"
    txt2 += ")"
    txt2 = txt2[:len(txt2)-2]+")"
    print(f"""INSERT INTO users {txt1} VALUES {txt2}""")
    cur.execute(f"""INSERT INTO users {txt1} VALUES {txt2}""")

con.commit()
con.close()
