import sqlite3

from song import Song


class Playlist:
    def __init__(self):
        self.id = None
        self.name = None
        self.description = None

    def load(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Playlist where id ={} """.format(self.id))
        result = s.fetchall()
        # print(result)
        self.name = result[0][1]
        self.description = result[0][2]

    def save(self, name="", describtion=""):   #Playlist_song_id deleted as a parameter
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Playlist VALUES(?, ?, ?)""", (self.id, name, describtion))
        conn.commit()

    def get_songs(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT song_id FROM Playlist_Song WHERE playlist_id={}""".format(self.id))
        ids = s.fetchall()
        songs = []
        for i in ids:
            new_song = Song(i[0])
            new_song.load()
            songs.append(new_song)
        return songs

    def __str__(self):
        return self.name + '\n' + self.description + '\n' + str([(i.name, i.length) for i in self.get_songs()])

    @staticmethod
    def get_all_playlist():
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT id FROM Playlist""")
        ids = s.fetchall()
        playlists = []
        for i in ids:
            new_playlist = Playlist(i[0])
            new_playlist.load()
            playlists.append(new_playlist)
        return playlists


if __name__ == '__main__':
    x = Playlist(1)
    x.save("suicidal", "when you have a suicidal thoughts")
    #x.load()
    #print(x)
