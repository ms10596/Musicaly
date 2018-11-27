import sqlite3


class Band:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.band_artist_id = None

    def load(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Band where id ={} """.format(self.id))
        result = s.fetchall()
        self.name = result[1]
        self.band_artist_id[2]

    def save(self, name="", band_artist_id=""):
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Band VALUES(?, ?, ?)""", (self.id, name, band_artist_id))
        conn.commit()


if __name__ == '__main__':
    x = Band(0)
    x.save("mshro3")
    x.load()
