import sqlite3

from album import Album
from artist import Artist
from band import Band
from genre import Genre


class Song:
    def __init__(self):
        self.id = None
        self.name = None
        self.release_date = None
        self.lyrics = None
        self.length = None
        self.album = None
        self.artist_id = None
        self.ft_id = None
        self.artist_type = None
        self.ft_type = None
        self.genre = []

    def load(self, id):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("SELECT * FROM Song where ID = ?", (id,))
        result = s.fetchall()
        self.name = result[0][1]
        self.release_date = result[0][2]
        self.lyrics = result[0][3]
        self.length = result[0][4]
        self.album = result[0][5]
        self.artist_id = result[0][6]
        self.artist_type = result[0][7]
        self.ft_type = result[0][8]
        self.ft_id = result[0][9]

    def save(self, name="", release_date="", lyrics="", length=""):
        conn = sqlite3.connect('../db/musicaly.db')
        params = (name, release_date, lyrics, length)
        conn.execute("INSERT INTO Song (name, release_date, lyrics, length) VALUES (?, ?, ?, ?)", params)
        conn.commit()

    # def __str__(self):
    #     return "Song: " + self.name + "\nBand/Artist: " + str(
    #         self.get_artist()) + "\nFeatured artist/band: " + str(
    #         self.get_featured()) + "\nAlbum: " + str(
    #         self.get_album()) + "\nRelease date: " + str(self.release_date) + "\nGenres: " + str(self.get_genre())

    def get_featured(self):
        if self.ft_type == "Artist":
            artist = Artist()
            artist.load(self.ft_id)
            return artist
        elif self.ft_type == "Band":
            band = Band()
            band.load(self.ft_id)
            return band
        else:
            return "No"

    def get_artist(self):
        if self.artist_type == "Artist":
            artist = Artist()
            artist.load(self.artist_id)
            return artist
        elif self.artist_type == "Band":
            band = Band()
            band.load(self.artist_id)
            return band
        else:
            return "unknown"

    # def get_album(self):
    #     conn = sqlite3.connect('db/musicaly.db')
    #     s = conn.execute("SELECT album_id FROM Album_Song WHERE song_id=?", (self.id,))
    #     album_id = s.fetchall()[0][0]
    #     # print(album_id)
    #     album = Album()
    #     album.load()
    #     return album

    def get_genre(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("SELECT GENRE_ID from Genre_Song WHERE SONG_ID =?", (self.id,))
        genre_id = s.fetchall()
        genres = []
        for i in genre_id:
            new_genre = Genre()
            new_genre.load(i[0])
            genres.append(new_genre.name)
        return genres

    def get_song_by_name(self, name):
        conn = conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("SELECT * FROM Song WHERE NAME=?", (name,))
        result = s.fetchall()
        song = Song()
        song.id = result[0][0]
        song.name = result[0][1]
        song.release_date = result[0][2]
        song.lyrics = result[0][3]
        song.length = result[0][4]
        song.album = result[0][5]
        song.artist_id = result[0][6]
        song.artist_type = result[0][7]
        song.ft_id = result[0][8]
        song.ft_type = result[0][9]
        return song

    def get_all_songs(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * from Song""")
        result = s.fetchall()
        songs = []
        for i in range(len(result)):
            song = Song()
            song.id = result[i][0]
            song.name = result[i][1]
            song.release_date = result[i][2]
            song.lyrics = result[i][3]
            song.length = result[i][4]
            song.album = result[i][5]
            song.artist_id = result[i][6]
            song.artist_type = result[i][7]
            song.ft_id = result[i][8]
            song.ft_type = result[i][9]
            songs.append(song)
        return songs


if __name__ == '__main__':
    s1 = Song(1)
    s1.load()
    print(s1)
    # s0.save("Bad Together.mp3", "2017", "", 238)
    # s1 = Song(1)
    # s1.save("Be The One.mp3", "2017", "", 204)
    # s2 = Song(2)
    # s2.save("Begging.mp3", "2017", "", 194)
    # s3 = Song(3)
    # s3.save("Blow Your Mind.mp3", "2017", "", 173)
