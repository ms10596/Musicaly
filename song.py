import pygame
import time
import sqlite3


class Song:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.release_date = None
        self.lyrics = None
        self.length = None
        self.artist_song_id = None
        self.band_song_id = None
        self.album_id = None
        self.genre_song_id = None
        # pygame.init()
        # pygame.mixer.music.load(self.name + '.mp3')

    def play(self):
        pygame.mixer.music.play()
        time.sleep(1000)

    def pause(self):
        pygame.mixer.music.pause()

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

    def save_song(self, name="", release_date="", lyrics="", length="", artist_song_id="", band_song_id="", album_id="",
                  genre_song_id=""):
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Song values(?, ?, ?, ?, ?, ?, ?, ?, ?)""", (
            self.id, name, release_date, lyrics, length, artist_song_id, band_song_id, album_id, genre_song_id))
        conn.commit()


if __name__ == '__main__':
    x = Song(0)
    x.load_song()
