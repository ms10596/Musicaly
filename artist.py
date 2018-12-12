import sqlite3


class Artist:
    def __init__(self):
        self.id = None
        self.name = None
        self.dob = None

    def load(self, id):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Artist where id=? """, (id,))
        result = s.fetchall()
        if len(result) == 0:
            return "not found"
        self.name = result[0][1]
        self.dob = result[0][2]
        conn.close()

    def save(self, name="", dob="", band_id=""):
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Artist VALUES(?, ?, ?)""", (name, dob, band_id))
        conn.commit()
        conn.close()

    def __str__(self):
        return str(self.name) + " " + str(self.dob)

    def get_songs(self):
        import song
        import band
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT id FROM Song WHERE ARTIST_TYPE ='Artist' AND (ARTIST_ID=? OR FT_ID=?)""",
                         (self.id, self.id,))
        songs_id = s.fetchall()
        songs = []
        for i in songs_id:
            new_song = song.Song()
            new_song.load(i[0])
            songs.append(new_song)

        s = conn.execute("""SELECT BAND_ID FROM Band_Artist WHERE ARTIST_ID=?""", (self.id,))
        bands_id = s.fetchall()
        if len(bands_id) > 0:
            for i in bands_id:
                band = band.Band(i[0])
                sgs = band.get_songs()
                songs = songs + sgs

        return songs

    def get_artist_by_name(self, name):
        conn = conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("SELECT * FROM Artist WHERE NAME=?", (name,))
        result = s.fetchall()
        ar = Artist()
        ar.id = result[0][0]
        ar.name = result[0][1]
        ar.dob = result[0][2]
        return ar



    @staticmethod
    def get_all_artists():
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Artist""")
        result = s.fetchall()
        artists = []
        for i in range(len(result)):
            new_artist = Artist()
            new_artist.id = result[i][0]
            new_artist.name = result[i][1]
            new_artist.dob = result[i][2]
            artists.append(new_artist)
        return artists


if __name__ == '__main__':
    for i in Artist.get_all_artists():
        print(i)
