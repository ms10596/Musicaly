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
        from song import Song
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT id FROM Song where artist_id =? OR ft_id=?""", (self.id, self.id,))
        songs_id = s.fetchall()
        songs = []
        for i in songs_id:
            new_song = Song(i[0])
            new_song.load()
            songs.append(new_song)
        return songs

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
