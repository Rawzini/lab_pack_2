import sqlite3

from werkzeug.security import generate_password_hash

connection = sqlite3.connect('../database.db')


with open('users.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (name, username, email, password_hash, role) VALUES (?, ?, ?, ?, ?)",
            ('Иван', 'IvanTheAdmin', 'ivan@teashort.com', generate_password_hash('password'), 'admin'))

cur.execute("INSERT INTO users (name, username, email, password_hash, role) VALUES (?, ?, ?, ?, ?)",
            ('НеИван', 'SuperUser', 'user@teashort.com', generate_password_hash('superpassword'), 'user'))

connection.commit()
connection.close()


