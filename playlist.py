import sqlite3

from song import Song


class Playlist:
    def __init__(self):
        self.id = None
        self.name = None
        self.description = None
        self.numOfSongs = None

    def load(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Playlist Where id""".format(self.id))
        result = s.fetchall()
        self.id = result[0][0]
        self.name = result[0][1]
        self.description = result[0][2]

    def save(self, name="", describtion=""): #deleted playlist_song_id as an argument
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Playlist VALUES(?, ?, ?)""", (self.id, name, describtion))
        conn.commit()

    def get_songs(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT SONG_ID FROM Playlist_Song WHERE PLAYLIST_ID=?""", (self.id,))
        ids = s.fetchall()
        songs = []
        for i in ids:
            new_song = Song()
            new_song.load(i[0])
            songs.append(new_song)
        return songs

    def __str__(self):
        return self.name + '\n' + self.description + '\n' + str([(i.name, i.length) for i in self.get_songs()])
    
    def addSongByName(self, playlistname, songName):    #adding songs by name to playlist by name
        conn = sqlite3.connect('db/musicaly.db')
        song = conn.execute("SELECT ID FROM Song WHERE NAME=?", (songName,))
        SongId = song.fetchone()
        play = conn.execute("SELECT ID FROM Playlist WHERE NAME=?", (playlistname,))
        playID = play.fetchone()
        #print(playID, SongId)
        conn.execute("INSERT INTO Playlist_Song VALUES(?, ?)", (playID[0], SongId[0],))
        conn.commit()
    

    def get_list_by_name(self, name):
        conn = conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("SELECT * FROM Playlist WHERE NAME=?", (name,))
        result = s.fetchall()
        playlist = Playlist()
        playlist.id = result[0][0]
        playlist.name = result[0][1]
        playlist.description = result[0][2]
        return playlist

    @staticmethod
    def get_all_playlist():
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Playlist""")
        result = s.fetchall()
        playlists = []
        for i in range(len(result)):
            new_playlist = Playlist()
            new_playlist.id = result[i][0]
            new_playlist.name = result[i][1]
            new_playlist.description = result[i][2]
            numOfsongs = conn.execute("SELECT * FROM Playlist_Song WHERE playlist_id=?", (result[i][0],))
            playlist_songs = numOfsongs.fetchall()
            new_playlist.numOfSongs = len(playlist_songs)
            playlists.append(new_playlist)
        return playlists


if __name__ == '__main__':
    x = Playlist()
    x.load()
    print(x)
    #x.save("sad", "sad when I am sad")
    x.addSongByName("sucidal", "Garden")
    #x.load()
    #print(x)