import sqlite3

connection = sqlite3.connect('../database.db')


with open('posts_add_photo_id_column.sql') as f:
    connection.executescript(f.read())

with open('photos.sql') as f:
    connection.executescript(f.read())

with open('comments.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()