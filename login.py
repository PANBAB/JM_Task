import sqlite3
import os

connect=sqlite3.connect('mydatabase.db')

cursor=connect.cursor()
users = {
    "admin": {
        "username": "admin",
        "password": "password"
    },
    "user": {
        "username": "user",
        "password": "password"
    },
}

def check_credentials(username, password, user_type):
    if user_type in users and users[user_type][
            "username"] == username and users[user_type][
                "password"] == password:
        return True
    return False


def admin_login():
    if request.method == "POST":
        username = request.form["admin_username"]
        password = request.form["admin_password"]
        if check_credentials(username, password, "admin"):
            return redirect(
                url_for(
                    "C:\Users\Ante\Downloads\Filmovi\ZADATAK\lpadmin.html"))


cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, user_type TEXT)"
)

cursor.execute(
    "INSERT INTO users (username, password, user_type) VALUES (?, ?, ?)",
    ("apb", "gusar10", "admin"))
conn.commit()


def check_credentials(username, password, user_type):
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=? AND user_type=?",
        (username, password, user_type),
    )
    user = cursor.fetchone()
    if user:
        return True
    return False


def admin_login():
    if request.method == "POST":
                username = request.form["admin_username"]
        password = request.form["admin_password"]
    if check_credentials(username, password, "admin"):
                 return redirect(url_for("C:\Users\Ante\Downloads\Filmovi\ZADATAK\lpadmin.html"))
    else:
                return "Invalid username or password"

conn.close()