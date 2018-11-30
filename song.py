import sqlite3

from album import Album
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

    def load_song(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("SELECT * FROM Song where id = {}".format(self.id))
        result = s.fetchall()
        self.name = result[1]
        self.release_date = result[2]
        self.lyrics = result[3]
        self.length = result[4]

    def save_song(self, name="", release_date="", lyrics="", length=""):
        conn = sqlite3.connect('db/musicaly.db')
        params = (self.id, name, release_date, lyrics, length)
        conn.execute("INSERT INTO Song (id,name, release_date, lyrics, length) VALUES (?,?, ?, ?, ?)", params)
        conn.commit()

    def __str__(self):
        return "Song: " + self.name + "\nBand/Artist: " + str(
            self.get_artist_band()) + "\nFeatured artist/band: " + str(
            self.get_featured()) + "Album: " + str(
            self.get_album()) + "\nRelease date: " + self.release_date + "\nGenres: " + str(self.get_genre())

    def get_featured(self):
        pass

    def get_artist_band(self):
        pass

    def get_album(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("SELECT album_id FROM Album_Song WHERE song_id={}".format(self.id))
        album_id = s.fetchall()[0]
        album = Album(album_id)
        album.load()
        return album

    def get_genre(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("SELECT genre_id from Genre_Song WHERE song_id ={}".format(self.id))
        genre_id = s.fetchall()[0]
        g = Genre(genre_id)
        g.load()
        return g


if __name__ == '__main__':
    s0 = Song(0)
    # s0.save_song("Bad Together .mp3", "2017", "", 238, 0)
    # s1 = Song(1)
    # s1.save_song("Be The One .mp3", "2017", "", 204, 0)
    # s2 = Song(2)
    # s2.save_song("Begging .mp3", "2017", "", 194, 0)
    # s3 = Song(3)
    # s3.save_song("Blow Your Mind .mp3", "2017", "", 173, 0)
