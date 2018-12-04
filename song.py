import sqlite3

from album import Album
from artist import Artist
from band import Band
from genre import Genre


class Song:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.release_date = None
        self.lyrics = None
        self.length = None
        self.artist_id = None
        self.ft_id = None
        self.artist_type = None
        self.ft_type = None

    def load(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("SELECT * FROM Song where id = {}".format(self.id))
        result = s.fetchall()
        self.name = result[0][1]
        self.release_date = result[0][2]
        self.lyrics = result[0][3]
        self.length = result[0][4]
        self.artist_id = result[0][6]
        self.artist_type = result[0][7]
        self.ft_type = result[0][8]
        self.ft_id = result[0][9]

    def save(self, name="", release_date="", lyrics="", length=""):
        conn = sqlite3.connect('db/musicaly.db')
        params = (self.id, name, release_date, lyrics, length)
        conn.execute("INSERT INTO Song (id, name, release_date, lyrics, length) VALUES (?, ?, ?, ?, ?)", params)
        conn.commit()

    def __str__(self):
        return "Song: " + self.name + "\nBand/Artist: " + str(
            self.get_artist()) + "\nFeatured artist/band: " + str(
            self.get_featured()) + "\nAlbum: " + str(
            self.get_album()) + "\nRelease date: " + str(self.release_date) + "\nGenres: " + str(self.get_genre())

    def get_featured(self):
        # print(self.ft_type)
        if self.ft_type == "artist":
            # print(self.ft_id)
            artist = Artist(self.ft_id)
            artist.load()
            return artist
        elif self.ft_type == "band":
            band = Band(self.ft_id)
            band.load()
            return band
        else:
            return "unkown"

    def get_artist(self):
        # print(self.artist_type)
        if self.artist_type == "artist":

            artist = Artist(self.artist_id)
            artist.load()
            return artist
        elif self.artist_type == "band":
            band = Band(self.artist_type)
            band.load()
            return band
        else:
            return "unkown"

    def get_album(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("SELECT album_id FROM Album_Song WHERE song_id={}".format(self.id))
        album_id = s.fetchall()[0][0]
        # print(album_id)
        album = Album(album_id)
        album.load()
        return album

    def get_genre(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("SELECT genre_id from Genre_Song WHERE song_id ={}".format(self.id))
        genre_id = s.fetchall()
        genres = []
        for i in genre_id:
            new_genre = Genre(i[0])
            new_genre.load()
            genres.append(new_genre.name)
        return genres


if __name__ == '__main__':
    s1 = Song(1)
    s1.load()
    print(s1)
    #s0.save("Bad Together.mp3", "2017", "", 238)
    #s1 = Song(1)
    #s1.save("Be The One.mp3", "2017", "", 204)
    #s2 = Song(2)
    #s2.save("Begging.mp3", "2017", "", 194)
    #s3 = Song(3)
    #s3.save("Blow Your Mind.mp3", "2017", "", 173)