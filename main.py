import sqlite3

qry = open("db/musicaly.sql").read()
# print(qry)
conn = sqlite3.connect('db/musicaly.db')
conn.executescript(qry)

