import sqlite3
import re
import os
import pygame
import urllib.request
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
        #get the real path of the song
        path = os.path.realpath(files)

        #load the song
        audio = eyed3.load(path)

        #print the the name of the artist
        print(audio.tag.artist)
        artist = str(audio.tag.artist)
        artist = artist.lower()
        artist = artist.replace(" ", "")

        #print the the title of the song
        print(audio.tag.title)
        song = str(audio.tag.title).replace(".mp3", "").lower()
        song = re.sub('[^0-9a-zA-Z]+', '', song)

        #to get the lyrics of the song from azlyrics
        url = "http://www.azlyrics.com/lyrics/" + artist + "/" + song + ".html"
        text = urllib.request.urlopen(url)
        lyrics = text.read()
        lyrics = str(lyrics)
        where_start = lyrics.find('<!-- Usage of azlyrics.com content by any third-party')
        start = where_start + 150
        where_end = lyrics.find('<!-- MxM banner -->')
        end = where_end - 32
        lyrics = lyrics[start:end].replace("<br>\\n", "\n")
        lyrics = lyrics.replace("\\'", "\'")
        lyrics = lyrics.replace("<i>", "")
        lyrics = lyrics.replace("</i>", "")
        print(lyrics)

        print(audio.tag.album)
        print(audio.tag.track_num)
        print(audio.tag.release_date)
        audio.tag.lyrics.set(lyrics)
        print(audio.tag.lyrics[0].text)
        print(audio.tag.genre.name)
        print(audio.info.time_secs)

        # sng = Song(audio.tag.track_num)
        # sng.save_song(name=audio.tag.artist)


