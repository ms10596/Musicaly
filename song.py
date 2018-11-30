import pygame
import time
import sqlite3


class Song:
    def __init__(self):
        self.id = None
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
        self.artist_song_id = result[5]
        self.band_song_id = result[6]
        self.album_id = result[7]
        self.genre_song_id = result[8]

    def save_song(self, name="", release_date="", lyrics="", length="", album=""):
        conn = sqlite3.connect('../db/musicaly.db')
        params = (name, release_date, lyrics, length, album)
        conn.execute("INSERT INTO Song (name, release_date, lyrics, length, album) VALUES (?, ?, ?, ?, ?)", params)
        conn.commit()


if __name__ == '__main__':
    x = Song(0)
    x.load_song()
