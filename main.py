import os
import re
import sqlite3
import urllib.request
import tkinter as tk
from tkinter.filedialog import askdirectory
from song import Song
from playlist import Playlist
import eyed3



qry = open("db/musicaly.sql").read()
conn = sqlite3.connect('db/musicaly.db')
conn.executescript(qry)

directory = askdirectory()
os.chdir(directory)
def window():
    root = tk.Tk()
    root.title("Musicaly")
    root.geometry('400x300')
    root.configure(bg="black")

    leftFrame = tk.Frame(root, bg = "black")
    leftFrame.grid(row = 0)

    lab = tk.Label(root, text = showplaylists(), bg = "Black", fg = "white")
    lab.grid(row = 0, column =  2)
    button1 = tk.Button(leftFrame, text = "Playlists", fg = "white", bg = "Black", width=20, command=showplaylists)
    button2 = tk.Button(leftFrame, text = "Albums", fg = "white", bg = "Black", width=20)
    button3 = tk.Button(leftFrame, text = "Artists", fg = "white", bg = "Black", width=20)

    button1.grid(row = 1, ipadx = 10, pady= 5, sticky=tk.NSEW)
    button2.grid(row = 2, ipadx = 10, pady= 5)
    button3.grid(row = 3, ipadx = 10, pady= 5)


    root.mainloop()


def main():



for files in os.listdir(directory):
    if files.endswith(".mp3"):
        # get the real path of the song
        path = os.path.realpath(files)

        # load the song
        audio = eyed3.load(path)

        # print the the name of the artist
        print(audio.tag.artist)
        artist = str(audio.tag.artist)
        artist = artist.lower()
        artist = artist.replace(" ", "")

        # print the the title of the song
        print(audio.tag.title)
        song = str(audio.tag.title).replace(".mp3", "").lower()
        song = tk.re.sub('[^0-9a-zA-Z]+', '', song)

        # to get the lyrics of the song from azlyrics
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
