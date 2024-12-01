from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
import sqlite3 as sq

app = Flask(__name__)

con = sq.connect("database.db", check_same_thread=False)
cur = con.cursor()


a = {"depart":[],"subd":[],"proj":[],"duty":[],"role":[],"city":[],"sex":[],"age":[],"age1":[]}
dk = [
    "Департамент",
    "Подразделение",
    "Проект",
    "Должность",
    "Роль",
    "Город",
    "Пол",
    "Возраст от",
    "Возраст до"
]

for i in a:
    if i == "age1":
        a["age1"].insert(0, '')
        break
    a[i].append("")
    cur.execute(f"""SELECT {i} FROM users""")
    k = cur.fetchall()
    for j in k:
        if not j[0] in a[i] and j[0] != "nan":
            if i == "age":
                a[i].append(j[0])
                a["age1"].append(j[0])
            else:
                a[i].append(j[0])

for i in a:
    a[i].sort()
    
lg = [
    "Должность",
    "Имя",
    "Фамилия",
    "Номер телефона",
    "Город",
    "Пол"
]
    
@app.route("/")
def start():
    return redirect(url_for('main'))

@app.route("/main")
def main():
    return render_template("index.html", a=a, k=dk, spis=1, hds=lg)

@app.route("/submit", methods=["POST"])
def submit():
    
    data = {
        "depart":request.form["depart"],
        "subd":request.form["subd"],
        "proj":request.form["proj"],
        "duty":request.form["duty"],
        "role":request.form["role"],
        "city":request.form["city"],
        "sex":request.form["sex"],
        "age":request.form["age"],
        "age1":request.form["age1"]
    }

    asd = {
        "depart":"Департамент",
        "subd":"Подразделение",
        "proj":"Проект",
        "duty":"Должность",
        "role":"Роль",
        "city":"Город",
        "sex":"Пол",
        "age":"Возраст"
    }

    req = " WHERE "
    p = 0
    for i in data:
        if data[i] != '' and i != "age" and i != "age1":
            req += f"{i}='{data[i]}' AND "
            p += 1
        if data[i] != '' and (i == "age" or i == "age1"):
            if i == "age":
                req += f"{i}>='{data[i]}' AND "
            else:
                req += f"age<='{data[i]}' AND "
                

    if p >= len(data):
        req = ""
    else:
        req = req[:len(req)-5]
    print(req)
    cur.execute(f"""SELECT duty,Имя,Фамилия,Телефон,city,sex FROM users{req}""")
    k = cur.fetchall()
            
    return render_template("index.html", a=a, k=dk, spis=k, hds=lg)
        
app.run(port=1200)
con.close()
