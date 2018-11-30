import sqlite3


class Album:
    def __init__(self, id):
        self.id = id
        self.title = None
        # self.band_id = None
        self.songs_no = None
        # self.album_song_id = None

    def load(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Album where id ={} """.format(self.id))
        result = s.fetchall()
        self.title = result[0][1]
        # self.band_id = result[2]
        self.songs_no = result[0][2]
        # self.album_song_id = result[4]
        # print(s.fetchall())

    def save(self, title="", song_no=""):
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Album VALUES(?, ?, ?)""", (self.id, title, song_no))
        conn.commit()

    def __str__(self):
        return str(self.title) + " " + str(self.songs_no)


if __name__ == '__main__':
    a0 = Album(0)
    # a0.save("dua lipa", 17)
    a0.load()
    print(a0)
