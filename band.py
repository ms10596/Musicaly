import sqlite3


class Band:
    def __init__(self, id):
        self.id = id

    def load(self):
        conn = sqlite3.connect('musicaly.db')
        s = conn.execute("""SELECT * FROM Band where id ={} """.format(self.id))
        print(s.fetchall())

    def save(self, name="", band_artist_id=""):
        conn = sqlite3.connect('musicaly.db')
        conn.execute("""INSERT INTO Band VALUES(?, ?, ?)""", (self.id, name, band_artist_id))
        conn.commit()
if __name__ == '__main__':
    x = Band(0)
    x.save("mshro3")
    x.load()
