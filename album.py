import sqlite3


class Album:
    def __init__(self, id):
        self.id = id

    def load(self):
        conn = sqlite3.connect('musicaly.db')
        s = conn.execute("""SELECT * FROM Album where id ={} """.format(self.id))
        print(s.fetchall())

    def save(self, title="", band_id="", song_no="", album_song_id=""):
        conn = sqlite3.connect('musicaly.db')
        conn.execute("""INSERT INTO Album VALUES(?, ?, ?, ?, ?)""", (self.id, title, band_id, song_no, album_song_id))
        conn.commit()


if __name__ == '__main__':
    x = Album(0)
    x.save("ibneleel")
    x.load()
