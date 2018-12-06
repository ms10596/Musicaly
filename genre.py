import sqlite3


class Genre:
    def __init__(self):
        self.id = None
        self.name = None

    def load(self, id):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Genre where ID = ?""", (id,))
        result = s.fetchall()
        self.name = result[0][1]

    def save(self, name):
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Genre VALUES(?, ?)""", (self.id, name))
        conn.commit()

    def __str__(self):
        return self.name

    def get_songs(self):
        from song import Song
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT song_id FROM Genre_Song where genre_id ={}""".format(self.id))
        songs_id = s.fetchall()
        songs = []
        for i in songs_id:
            new_song = Song(i[0])
            new_song.load()
            songs.append(new_song)
        return songs


if __name__ == '__main__':
    g2 = Genre(2)
    g2.save("arabic")
