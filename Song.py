import pygame
import time


class Song:
    def __init__(self, name="", band="", featured_artists="", album="", release_date="", genres="", lyrics="",
                 length=""):
        pygame.init()
        self.name = name
        self.band = band
        self.featured_artists = featured_artists
        self.album = album
        self.release_date = release_date
        self.genres = genres
        self.lyrics = lyrics
        self.length = length
        pygame.mixer.music.load(self.name + '.mp3')

    def play(self):
        pygame.mixer.music.play()
        time.sleep(1000)

    def pause(self):
        pygame.mixer.music.pause()


if __name__ == '__main__':
    x = Song('Sufi Hop')
    x.play()
    x.pause()
