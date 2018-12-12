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
        import song
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT SONG_ID FROM Genre_Song where GENRE_ID = ?""", (self.id,))
        songs_id = s.fetchall()
        songs = []
        for i in songs_id:
            new_song = song.Song()
            new_song.load(i[0])
            songs.append(new_song)
        return songs

    def get_all_genres(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * from Genre""")
        result = s.fetchall()
        genres = []
        for i in range(len(result)):
            genre = Genre()
            genre.id = result[i][0]
            genre.name = result[i][1]
            genres.append(genre)
        return genres

    def get_genre_by_name(self, name):
        conn = conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("SELECT * FROM Genre WHERE NAME=?", (name,))
        result = s.fetchall()
        gn = Genre()
        gn.id = result[0][0]
        gn.name = result[0][1]
        return gn


if __name__ == '__main__':
    g2 = Genre(2)
    g2.save("arabic")
