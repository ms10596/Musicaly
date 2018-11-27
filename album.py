import sqlite3


class Album:
    def __init__(self, id):
        self.id = id
        self.title = None
        self.band_id = None
        self.songs_no = None
        self.album_song_id = None

    def load(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Album where id ={} """.format(self.id))
        result = s.fetchall()
        self.title = result[1]
        self.band_id = result[2]
        self.songs_no = result[3]
        self.album_song_id = result[4]
        # print(s.fetchall())

    def save(self, title="", band_id="", song_no="", album_song_id=""):
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Album VALUES(?, ?, ?, ?, ?)""", (self.id, title, band_id, song_no, album_song_id))
        conn.commit()


if __name__ == '__main__':
    x = Album(0)
    x.save("ibneleel")
    x.load()
