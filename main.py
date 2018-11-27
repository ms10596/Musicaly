import sqlite3

qry = open("musicaly").read()
# print(qry)
conn = sqlite3.connect('musicaly.db')
# conn.executescript(qry)
# conn.execute("""Insert into Artist(id, name, dob, band_id) VALUES (1, 'sayed', '1/4/5', 1)""")
# conn.commit()
