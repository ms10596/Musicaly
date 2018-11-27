import pygame
import time
import sqlite3


class Song:
    def __init__(self, id):
        self.id = id

        # pygame.init()
        # pygame.mixer.music.load(self.name + '.mp3')

    def play(self):
        pygame.mixer.music.play()
        time.sleep(1000)

    def pause(self):
        pygame.mixer.music.pause()

    def load_song(self):
        conn = sqlite3.connect('musicaly.db')
        s = conn.execute("""SELECT * FROM Song where id =0 """)
        print(s.fetchall())

    def save_song(self):
        conn = sqlite3.connect('musicaly.db')
        conn.execute("""INSERT INTO Song(id, name) values(0, 'love')""")
        conn.commit()


if __name__ == '__main__':
    x = Song(0)
    x.load_song()
