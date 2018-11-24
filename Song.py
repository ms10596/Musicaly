class Song:
    def __init__(self, name="", band="", featured_artists="", album="", release_date="", genres="", lyrics="", length=""):
        self.name = name
        self.band = band
        self.featured_artists = featured_artists
        self.album = album
        self.release_date = release_date
        self.genres = genres
        self.lyrics = lyrics
        self.length = length

    def play(self):
        import pygame
        import time
        pygame.init()
        pygame.mixer.music.load(self.name + '.mp3')
        pygame.mixer.music.play()
        time.sleep(1000)


if __name__ == '__main__':
    x = Song('Sufi Hop')
    x.play()