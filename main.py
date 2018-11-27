import sqlite3
import os
import pygame
import eyed3
from tkinter.filedialog import askdirectory
from song import Song

qry = open("db/musicaly.sql").read()
conn = sqlite3.connect('db/musicaly.db')
conn.executescript(qry)

directory = askdirectory()
os.chdir(directory)

for files in os.listdir(directory):
    if files.endswith(".mp3"):
        path = os.path.realpath(files)
        audio = eyed3.load(path)
        print(audio.tag.artist)
        print(audio.tag.title)
        print(audio.tag.album)
        print(audio.tag.track_num)
        print(audio.tag.release_date)
        print(audio.tag.lyrics)
        print(audio.tag.genre.name)
        print(audio.info.time_secs)
        # sng = Song(audio.tag.track_num)
        # sng.save_song(name=audio.tag.artist)


