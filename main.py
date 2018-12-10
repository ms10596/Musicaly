import os, time
import re
import eyed3
import sqlite3
import urllib.request
import tkinter as tk
from tkinter.filedialog import askdirectory
from playlist import *
from song import *
from album import *
from artist import *
import datetime
import pygame

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


def playlist(playlists, listbox):
    listbox.delete(0, "end")
    listbox.insert("end", "Playlists")
    for i in range(len(playlists)):
        space = 40 - len(playlists[i].name)
        play = "* " + playlists[i].name + (" " * space) + "Tracks : " + str(playlists[i].numOfSongs)
        listbox.insert("end", play)


def album(albums, listbox):
    listbox.delete(0, "end")
    listbox.insert("end", "Albums")
    for i in range(len(albums)):
        al = "* " + albums[i].title + "        Tracks : " + str(albums[i].songs_no)
        listbox.insert("end", al)


def artist(artists, listbox):
    listbox.delete(0, "end")
    for i in range(len(artists)):
        art = "* " + artists[i].name
        listbox.insert("end", art)


def song(songs, listbox):
    listbox.delete(0, "end")
    listbox.insert("end", "Songs")
    for i in range(len(songs)):
        sg = "* " + songs[i].name
        listbox.insert("end", sg)


def description(listbox, des):
    des.delete(0, "end")
    if listbox.get(0) == "Songs":
        name = str(listbox.get(listbox.curselection()))
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
    elif listbox.get(0) == "Playlists":
        name = str(listbox.get(listbox.curselection()))
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


def playAlbum(listbox):
    if listbox.get(0) == "Albums":
        title = str(listbox.get(listbox.curselection()))
        n = title.split(" ")
        title = n[1] + " " + n[2]
        alb = Album()
        alb = alb.get_album_by_title(title)
        songs = alb.get_songs()
        listbox.delete(0, "end")
        listbox.insert("end", "Songs")
        numOfSongs = len(songs)
        title = title.replace(" ", "")
        os.system("touch " + title + ".m3u")
        listbox.insert("end", "* " + songs[0].name)
        os.system("echo " + songs[0].path + " > " + title + ".m3u")
        for i in range(1, numOfSongs, 1):
            listbox.insert("end", "* " + songs[i].name)
            os.system("echo " + songs[i].path + " >> " + title + ".m3u")

        os.system("killall play")
        os.system("play -q " + title + ".m3u &")
        listbox.select_set(1)


def plays(listbox):
    if listbox.get(0) == "Songs":
        name = str(listbox.get(listbox.curselection()))
        name = name[2:]
        sg = Song()
        sg = sg.get_song_by_name(name)
        os.system("killall play")
        os.system("play -q \"" + sg.path + "\" &")

        # e = eyed3.load(sg.path)
        # freq = e.info.sample_freq
        # pygame.mixer.pre_init(freq, -16, 2, 4096)
        # pygame.mixer.init()
        # pygame.mixer.music.load(sg.path)
        # pygame.mixer.music.play()
        # pygame.time.delay(1000)


def pause():
    os.system("killall play")


def next(listbox):
    current = listbox.curselection()[0]
    if current < listbox.size() - 1:
        listbox.select_clear(current)
        listbox.select_set(current + 1)
    plays(listbox)


def previous(listbox):
    current = listbox.curselection()[0]
    if current > 1:
        listbox.select_clear(current)
        listbox.select_set((current - 1))
    plays(listbox)


root = tk.Tk()
root.title("Musicaly")
root.geometry('800x520')
root.configure(bg="black")

leftFrame = tk.Frame(root, bg="black", height=600, width=25)
leftFrame.grid(row=0, column=0, sticky="n")

button1 = tk.Button(leftFrame, text="Songs", fg="white", bg="Black", width=20, command=lambda: song(songs, listbox))
button2 = tk.Button(leftFrame, text="Albums", fg="white", bg="Black", width=20, command=lambda: album(albums, listbox))
button3 = tk.Button(leftFrame, text="playlists", fg="white", bg="Black", width=20,
                    command=lambda: playlist(playlists, listbox))
button4 = tk.Button(leftFrame, text="Artists", fg="white", bg="Black", width=20,
                    command=lambda: artist(artists, listbox))
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
rightFrame.grid(row=0, column=2, sticky="n")

descriptionButt = tk.Button(rightFrame, text="description", fg="white", bg="black", width=15,
                            command=lambda: description(listbox, desList))
descriptionButt.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=5)

desList = tk.Listbox(rightFrame, height=10, width=48)
desList.grid(row=0, column=2, columnspan=5, padx=10, pady=5, sticky="e")

listbox = tk.Listbox(rightFrame, height=18, width=70)
listbox.grid(row=1, rowspan=4, columnspan=7, padx=10, pady=5, sticky="n")
listbox.bind('<Double-1>', lambda x: playAlbum(listbox))

prevSongButt = tk.Button(rightFrame, text="previous", fg="white", bg="black", width=5,
                         command=lambda: previous(listbox))
prevSongButt.grid(row=6, column=1, sticky="e")

playSongButt = tk.Button(rightFrame, text="play", fg="white", bg="black", width=5, command=lambda: plays(listbox))
playSongButt.grid(row=6, column=2, padx=3, sticky="e")

pauseSongButt = tk.Button(rightFrame, text="pause", fg="white", bg="black", width=5, command=lambda: pause())
pauseSongButt.grid(row=6, column=3, sticky="w")

nextSongButt = tk.Button(rightFrame, text="next", fg="white", bg="black", width=5, command=lambda: next(listbox))
nextSongButt.grid(row=6, column=4, sticky="w")

root.mainloop()

os.system("killall play")
directory = "/home/shehabeldeen/materials/concepts of programming/Musicaly/"
os.chdir(directory)
for files in os.listdir(directory):
    if files.endswith(".m3u"):
        os.remove(files)

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
#         # listbox.insert("end", song)
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
#         sng.save(name=title, release_date="2017", lyrics=lyrics, length=audio.info.time_secs, path=path)
