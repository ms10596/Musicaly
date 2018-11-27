import sqlite3


class Artist:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.dob = None

    def load(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Artist where id ={} """.format(self.id))
        result = s.fetchall()
        self.name = result[1]
        self.dob = result[2]

    def save(self, name="", dob="", band_id=""):
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Artist VALUES(?, ?, ?,?)""", (self.id, name, dob, band_id))
        conn.commit()


if __name__ == '__main__':
    x = Artist(1)
    # x.save("michael", "1/5/6", 0)

    x.load()

    # x.save("michael", "1/5/5", 1)
