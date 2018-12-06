import os
import inspect
import re
import sqlite3
import urllib.request
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory

import eyed3

qry = open("db/musicaly.sql").read()
conn = sqlite3.connect('db/musicaly.db')
conn.executescript(qry)


# directory = askdirectory()
directory = "/home/shehabeldeen/materials/concepts of programming/Musicaly/songs"
os.chdir(directory)

root = tk.Tk()
root.title("Musicaly")
root.geometry('800x600')
root.configure(bg="black")

leftFrame = tk.Frame(root, bg="black", height=600, width=25)
leftFrame.grid(column=0, sticky="n")

button1 = tk.Button(leftFrame, text="Songs", fg="white", bg="Black", width=20)
button2 = tk.Button(leftFrame, text="Albums", fg="white", bg="Black", width=20)
button3 = tk.Button(leftFrame, text="playlists", fg="white", bg="Black", width=20)
button4 = tk.Button(leftFrame, text="Artists", fg="white", bg="Black", width=20)
button5 = tk.Button(leftFrame, text="Bands", fg="white", bg="Black", width=20)
button6 = tk.Button(leftFrame, text="genre", fg="white", bg="Black", width=20)

button1.grid(row=0, padx=10, pady=5)
button2.grid(row=1, padx=10, pady=5)
button3.grid(row=2, padx=10, pady=5)
button4.grid(row=3, padx=10, pady=5)
button5.grid(row=4, padx=10, pady=5)
button6.grid(row=5, padx=10, pady=5)

separator = tk.Frame(root, bg="white", width=3, height=600)
separator.grid(row=0, column=1)

rightframe = tk.Frame(root, bg="black", width=400)
rightframe.grid(row=0, column=2)

list = tk.Listbox(rightframe, height=25, width=70)
list.grid(row=0, column=0, padx=10, pady=5, sticky="n")


for files in os.listdir(directory):
    if files.endswith(".mp3"):
        # get the real path of the song
        path = os.path.realpath(files)

        # load the song
        audio = eyed3.load(path)

        # print the the name of the artist
        # print(audio.tag.artist)
        artist = str(audio.tag.artist)
        artist = artist.lower()
        artist = artist.replace(" ", "")

        # print the the title of the song
        # print(audio.tag.title)
        song = str(audio.tag.title).replace(".mp3", "").lower()
        song = tk.re.sub('[^0-9a-zA-Z]+', '', song)
        list.insert("end", song)
        # print(artist, song)
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
        # print(lyrics)

        # print(audio.tag.album)
        # print(audio.tag.track_num)
        # print(audio.tag.release_date)
        audio.tag.lyrics.set(lyrics)
        # print(audio.tag.lyrics[0].text)
        # print(audio.tag.genre.name)
        # print(audio.info.time_secs)

        # sng = Song(audio.tag.track_num)
        # sng.save_song(name=audio.tag.artist)


root.mainloop()
