import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

#create a db consists of id - name
sql = """
DROP TABLE IF EXISTS users;
CREATE TABLE users (
id integer unique primary key autoincrement,
name text
);
"""

c.executescript(sql)

conn.commit()
conn.close()

