import sqlite3


class Band:
    def __init__(self, id=None):
        self.id = id
        self.name = None

    def load(self, id):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Band where id =? """, (id,))
        result = s.fetchall()
        if len(result) == 0:
            return "not found"
        self.name = result[0][1]

    def save(self, name=""):
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Band VALUES(?, ?)""", (self.id, name))
        conn.commit()

    def __str__(self):
        return self.name

    def get_songs(self):
        import song
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT ID FROM Song where ARTIST_TYPE ='Band' AND (ARTIST_ID=? OR FT_ID=?)""",
                         (self.id, self.id,))
        result = s.fetchall()
        songs = []
        for i in result:
            new_song = song.Song()
            new_song.load(i[0])
            songs.append(new_song)
        return songs

    def get_all_bands(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * from Band""")
        result = s.fetchall()
        bands = []
        for i in range(len(result)):
            band = Band()
            band.id = result[i][0]
            band.name = result[i][1]
            bands.append(band)
        return bands

    def get_band_by_name(self, name):
        conn = conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("SELECT * FROM Band WHERE NAME=?", (name,))
        result = s.fetchall()
        bd = Band()
        bd.id = result[0][0]
        bd.name = result[0][1]
        return bd


if __name__ == '__main__':
    x = Band(0)
    # x.save("mshro3")
    x.load()
    print(x)
