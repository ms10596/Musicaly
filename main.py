import os
import inspect
import re
import eyed3
import sqlite3
import urllib.request
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from playlist import *
from song import *
from album import *
from artist import *
import datetime

# ----- connect to database -------
qry = open("db/musicaly.sql").read()
conn = sqlite3.connect('db/musicaly.db')
conn.executescript(qry)

# ------------- GUI ---------------

playlist = Playlist()
playlists = playlist.get_all_playlist()

album = Album()
albums = album.get_all_albums()

artist = Artist()
artists = artist.get_all_artists()

song = Song()
songs = song.get_all_songs()


def playlist(playlists, list):
    list.delete(0, "end")
    list.insert("end", "Playlists")
    for i in range(len(playlists)):
        space = 40 - len(playlists[i].name)
        play = "* " + playlists[i].name + (" " * space) + "Tracks : " + str(playlists[i].numOfSongs)
        list.insert("end", play)


def album(albums, list):
    list.delete(0, "end")
    for i in range(len(albums)):
        al = "* " + albums[i].title + "        Tracks : " + str(albums[i].songs_no)
        list.insert("end", al)


def artist(artists, list):
    list.delete(0, "end")
    for i in range(len(artists)):
        art = "* " + artists[i].name
        list.insert("end", art)


def song(songs, list):
    list.delete(0, "end")
    list.insert("end", "Songs")
    for i in range(len(songs)):
        sg = "* " + songs[i].name
        list.insert("end", sg)


def description(list, des):
    des.delete(0, "end")
    if list.get(0) == "Songs":
        name = str(list.get(list.curselection()))
        name = name[2:]
        sg = Song()
        sg = sg.get_song_by_name(name)
        des.insert("end", "Song : " + name)
        des.insert("end", sg.artist_type + " : " + sg.get_artist().name)
        if sg.ft_type == None:
            des.insert("end", "Featured Artist : No")
        else:
            des.insert("end", "Featured " + sg.ft_type + " : " + sg.get_featured().name)
        des.insert("end", "Album : " + sg.album)
        des.insert("end", "Release date : " + str(sg.release_date))
        genres = sg.get_genre()
        genres = "".join(genres)
        des.insert("end", "Genres : " + genres)
    elif list.get(0) == "Playlists":
        name = str(list.get(list.curselection()))
        n = name.split(" ")
        name = n[1] + " " + n[2]
        pl = Playlist()
        pl = pl.get_list_by_name(name)
        des.insert("end", pl.name)
        des.insert("end", "  " + pl.description)
        songs = pl.get_songs()
        for i in range(len(songs)):
            des.insert("end",
                       songs[i].name + (" " * 10) + "Duration : " + str(datetime.timedelta(seconds=songs[i].length)))


root = tk.Tk()
root.title("Musicaly")
root.geometry('800x600')
root.configure(bg="black")

leftFrame = tk.Frame(root, bg="black", height=600, width=25)
leftFrame.grid(row=0, column=0, sticky="n")

button1 = tk.Button(leftFrame, text="Songs", fg="white", bg="Black", width=20, command=lambda: song(songs, list))
button2 = tk.Button(leftFrame, text="Albums", fg="white", bg="Black", width=20, command=lambda: album(albums, list))
button3 = tk.Button(leftFrame, text="playlists", fg="white", bg="Black", width=20,
                    command=lambda: playlist(playlists, list))
button4 = tk.Button(leftFrame, text="Artists", fg="white", bg="Black", width=20, command=lambda: artist(artists, list))
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

rightFrame = tk.Frame(root, bg="black", width=400)
rightFrame.grid(row=0, column=2)

descriptionButt = tk.Button(rightFrame, text="description", fg="white", bg="black", width=15,
                            command=lambda: description(list, desList))
descriptionButt.grid(row=0, column=0, sticky="w", padx=10, pady=5)

desList = tk.Listbox(rightFrame, height=10, width=50)
desList.grid(row=0, column=0, padx=10, pady=5, sticky="e")

list = tk.Listbox(rightFrame, height=25, width=70)
list.grid(row=1, column=0, padx=10, pady=5, sticky="n")

root.mainloop()

# directory = askdirectory()
# directory = "/home/shehabeldeen/materials/concepts of programming/Musicaly/songs"
# os.chdir(directory)
# for files in os.listdir(directory):
#     if files.endswith(".mp3"):
#         # get the real path of the song
#         path = os.path.realpath(files)
#
#         # load the song
#         audio = eyed3.load(path)
#
#         # print the the name of the artist
#         # print(audio.tag.artist)
#         artist = str(audio.tag.artist)
#         artist = artist.lower()
#         artist = artist.replace(" ", "")
#
#         # print the the title of the song
#         # print(audio.tag.title)
#         song = str(audio.tag.title).replace(".mp3", "").lower()
#         song = tk.re.sub('[^0-9a-zA-Z]+', '', song)
#         # list.insert("end", song)
#         # print(artist, song)
#         # to get the lyrics of the song from azlyrics
#         url = "http://www.azlyrics.com/lyrics/" + artist + "/" + song + ".html"
#         try:
#             text = urllib.request.urlopen(url)
#         except:
#             text = ""
#             pass
#         lyrics = text.read()
#         lyrics = str(lyrics)
#         where_start = lyrics.find('<!-- Usage of azlyrics.com content by any third-party')
#         start = where_start + 150
#         where_end = lyrics.find('<!-- MxM banner -->')
#         end = where_end - 32
#         lyrics = lyrics[start:end].replace("<br>\\n", "\n")
#         lyrics = lyrics.replace("\\'", "\'")
#         lyrics = lyrics.replace("<i>", "")
#         lyrics = lyrics.replace("</i>", "")
#         # print(lyrics)
#
#         # print(audio.tag.album)
#         # print(audio.tag.track_num)
#         # print(audio.tag.release_date)
#         audio.tag.lyrics.set(lyrics)
#         # print(audio.tag.lyrics[0].text)
#         # print(audio.tag.genre.name)
#         # print(audio.info.time_secs)
#
#         sng = Song()
#         title = str(audio.tag.title).replace(".mp3", "")
#         sng.save(name=title, release_date="2017", lyrics=lyrics, length=audio.info.time_secs)
