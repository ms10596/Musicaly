import sqlite3


class Album:
    def __init__(self, id):
        self.id = id
        self.title = None
        self.songs_no = None

    def load(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Album where id ={} """.format(self.id))
        result = s.fetchall()
        self.title = result[0][1]
        self.songs_no = result[0][2]

    def save(self, title="", song_no=""):
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Album VALUES(?, ?, ?)""", (self.id, title, song_no))
        conn.commit()

    def __str__(self):
        return str(self.title) + " " + str(self.songs_no)

    def get_songs(self):
        from song import Song
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT song_id FROM Album_Song where album_id ={} """.format(self.id))
        songs_id = s.fetchall()
        songs = []
        for i in songs_id:
            new_song = Song(i[0])
            new_song.load()
            songs.append(new_song)
        return songs

    @staticmethod
    def get_all_albums():
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT id from Album""")
        ids = s.fetchall()
        albums = []
        for i in ids:
            new_album = Album(i[0])
            new_album.load()
            albums.append(new_album)
        return albums


if __name__ == '__main__':
    for i in Album.get_all_albums():
        print(i)
