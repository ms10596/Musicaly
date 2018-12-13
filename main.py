import os, time
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
from band import *
from genre import *
import datetime

# import pygame

# ----- connect to database -------
qry = open("db/musicaly.sql").read()
conn = sqlite3.connect('db/musicaly.db')
conn.executescript(qry)


# ------------- GUI ---------------


def playlist(listbox):
    listbox.delete(0, "end")
    listbox.insert("end", "Playlists")
    playlist = Playlist()
    playlists = playlist.get_all_playlist()
    for i in range(len(playlists)):
        space = 40 - len(playlists[i].name)
        play = "* " + playlists[i].name + "Tracks : ".rjust(space) + str(playlists[i].numOfSongs)
        listbox.insert("end", play)


def album(listbox):
    listbox.delete(0, "end")
    listbox.insert("end", "Albums")
    album = Album()
    albums = album.get_all_albums()
    for i in range(len(albums)):
        al = "* " + albums[i].title + "        Tracks : " + str(albums[i].songs_no)
        listbox.insert("end", al)


def artist(listbox):
    listbox.delete(0, "end")
    listbox.insert("end", "Artists")
    artist = Artist()
    artists = artist.get_all_artists()
    for i in range(len(artists)):
        art = "* " + artists[i].name
        listbox.insert("end", art)


def song(listbox):
    listbox.delete(0, "end")
    listbox.insert("end", "Songs")
    song = Song()
    songs = song.get_all_songs()
    for i in range(len(songs)):
        sg = "* " + songs[i].name
        listbox.insert("end", sg)


def band(listbox):
    listbox.delete(0, "end")
    listbox.insert("end", "Bands")
    band = Band()
    bands = band.get_all_bands()
    for i in range(len(bands)):
        bd = "* " + bands[i].name
        listbox.insert("end", bd)


def genre(listbox):
    listbox.delete(0, "end")
    listbox.insert("end", "Genres")
    genre = Genre()
    genres = genre.get_all_genres()
    for i in range(len(genres)):
        gn = "* " + genres[i].name
        listbox.insert("end", gn)


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
        if sg.album != None:
            des.insert("end", "Album : " + sg.album)
        des.insert("end", "Release date : " + str(sg.release_date))
        genres = sg.get_genre()
        genres = ", ".join(genres)
        des.insert("end", "Genres : " + genres)
        des.insert("end", "lyrics :")
        des.insert("end", " ")
        lyrics = str(sg.lyrics).split("\n")
        for i in lyrics:
            desList.insert("end", i)
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
            space = 30 - len(songs[i].name)
            sg = str(songs[i].name).ljust(len(songs[i].name) + space) + "Duration : " + str(
                datetime.timedelta(seconds=songs[i].length))
            des.insert("end", sg)


def doubleclick(listbox):
    if listbox.get(0) == "Albums":
        playAlbum(listbox)
    elif listbox.get(0) == "Bands":
        playBand(listbox)
    elif listbox.get(0) == "Artists":
        playArtist(listbox)
    elif listbox.get(0) == "Genres":
        playGenre(listbox)
    elif listbox.get(0) == "Playlists":
        playPlaylist(listbox)


def playAlbum(listbox):
    title = str(listbox.get(listbox.curselection()))
    tr = title.find("Tracks")
    title = title[2:tr]
    title = title.strip()
    alb = Album()
    alb = alb.get_album_by_title(title)
    songs = alb.get_songs()
    listbox.delete(0, "end")
    listbox.insert("end", "Songs")
    numOfSongs = len(songs)
    title = tk.re.sub('[^0-9a-zA-Z]+', '', title)
    os.system("touch " + title + ".m3u")
    listbox.insert("end", "* " + songs[0].name)
    os.system("echo " + songs[0].path + " > " + title + ".m3u")
    for i in range(1, numOfSongs, 1):
        listbox.insert("end", "* " + songs[i].name)
        os.system("echo " + songs[i].path + " >> " + title + ".m3u")

    os.system("killall play")
    os.system("play -q " + title + ".m3u &")
    listbox.select_set(1)


def playBand(listbox):
    name = str(listbox.get(listbox.curselection()))
    name = name[2:]
    band = Band()
    band = band.get_band_by_name(name)
    songs = band.get_songs()
    numOfSongs = len(songs)
    listbox.delete(0, "end")
    listbox.insert("end", "Songs")
    name = tk.re.sub('[^0-9a-zA-Z]+', '', name)
    os.system("touch " + name + ".m3u")
    listbox.insert("end", "* " + songs[0].name)
    os.system("echo " + songs[0].path + " > " + name + ".m3u")
    for i in range(1, numOfSongs, 1):
        listbox.insert("end", "* " + songs[i].name)
        os.system("echo " + songs[i].path + " >> " + name + ".m3u")

    os.system("killall play")
    os.system("play -q " + name + ".m3u &")
    listbox.select_set(1)


def playArtist(listbox):
    name = str(listbox.get(listbox.curselection()))
    name = name[2:]
    artist = Artist()
    artist = artist.get_artist_by_name(name)
    songs = artist.get_songs()
    numOfSongs = len(songs)
    listbox.delete(0, "end")
    listbox.insert("end", "Songs")
    name = tk.re.sub('[^0-9a-zA-Z]+', '', name)
    os.system("touch " + name + ".m3u")
    listbox.insert("end", "* " + songs[0].name)
    os.system("echo " + songs[0].path + " > " + name + ".m3u")
    for i in range(1, numOfSongs, 1):
        listbox.insert("end", "* " + songs[i].name)
        os.system("echo " + songs[i].path + " >> " + name + ".m3u")

    os.system("killall play")
    os.system("play -q " + name + ".m3u &")
    listbox.select_set(1)


def playGenre(listbox):
    name = str(listbox.get(listbox.curselection()))
    name = name[2:]
    genre = Genre()
    genre = genre.get_genre_by_name(name)
    songs = genre.get_songs()
    numOfSongs = len(songs)
    listbox.delete(0, "end")
    listbox.insert("end", "Songs")
    name = tk.re.sub('[^0-9a-zA-Z]+', '', name)
    os.system("touch " + name + ".m3u")
    listbox.insert("end", "* " + songs[0].name)
    os.system("echo " + songs[0].path + " > " + name + ".m3u")
    for i in range(1, numOfSongs, 1):
        listbox.insert("end", "* " + songs[i].name)
        os.system("echo " + songs[i].path + " >> " + name + ".m3u")

    os.system("killall play")
    os.system("play -q " + name + ".m3u &")
    listbox.select_set(1)


def playPlaylist(listbox):
    name = str(listbox.get(listbox.curselection()))
    tr = name.find("Tracks")
    name = name[2:tr]
    name = name.strip()
    playlist = Playlist()
    playlist = playlist.get_list_by_name(name)
    songs = playlist.get_songs()
    listbox.delete(0, "end")
    listbox.insert("end", "Songs of playlist : " + name)
    numOfSongs = len(songs)
    name = tk.re.sub('[^0-9a-zA-Z]+', '', name)
    os.system("touch " + name + ".m3u")
    listbox.insert("end", "* " + songs[0].name)
    os.system("echo " + songs[0].path + " > " + name + ".m3u")
    for i in range(1, numOfSongs, 1):
        listbox.insert("end", "* " + songs[i].name)
        os.system("echo " + songs[i].path + " >> " + name + ".m3u")

    os.system("killall play")
    os.system("play -q " + name + ".m3u &")
    listbox.select_set(1)


def plays(listbox):
    if listbox.get(0) == "Songs" or str(listbox.get(0)).find("Songs of playlist") > -1:
        name = str(listbox.get(listbox.curselection()))
        name = name[2:]
        sg = Song()
        sg = sg.get_song_by_name(name)
        os.system("killall play")
        os.system("play -q \"" + sg.path + "\" &")


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


def addPlaylist():
    addwindow = tk.Tk()
    addwindow.title("Add new playlist")
    addwindow.geometry('250x100')
    addwindow.configure(bg="black")

    lbl1 = tk.Label(addwindow, text="Name", fg="white", bg="black").grid(row=0, column=0)
    lbl2 = tk.Label(addwindow, text="Description", fg="white", bg="black").grid(row=1, column=0)

    namebox = tk.Entry(addwindow)
    descriptionbox = tk.Entry(addwindow)

    namebox.focus()

    namebox.grid(row=0, column=1)
    descriptionbox.grid(row=1, column=1)

    newplaylist = Playlist()

    savebutton = tk.Button(addwindow, text="Add playlist", fg="white", bg="black",
                           command=lambda: newplaylist.save(namebox.get(), descriptionbox.get()))
    savebutton.grid(row=2, column=1, pady=10)

    addwindow.mainloop()


def addsongToplaylist(song_name):
    playlist = Playlist()
    playlists = playlist.get_all_playlist()
    playlis = ()
    for i in range(len(playlists)):
        playlis = playlis + (playlists[i].name,)

    addwindow = tk.Tk()
    addwindow.title("Add song to playlist")
    addwindow.geometry('250x70')
    addwindow.configure(bg="black")
    lbl1 = tk.Label(addwindow, text="Playlist:", fg="white", bg="black").grid(row=0, column=0)
    playlistmenu = ttk.Combobox(addwindow, values=playlis)
    playlistmenu.current(0)
    playlistmenu.grid(row=0, column=1, padx=10, pady=5)

    pl = Playlist()
    addSongbtn = tk.Button(addwindow, text="Add Song", fg="white", bg="black",
                           command=lambda: pl.addSongByName(playlistmenu.get(), song_name))
    addSongbtn.grid(row=1, column=1, padx=10, pady=5)
    addwindow.mainloop()


def removeSong(playlist_name, song_name):
    pl = Playlist()
    pl.removeSong(playlist_name, song_name)


def popmenu(listbox, x_root, y_root):
    if listbox.get(0) == "Songs":
        song_name = listbox.get(listbox.curselection())
        song_name = song_name[2:]
        menu = tk.Menu(tearoff=0)
        menu.add_command(label="Add to playlist", command=lambda: addsongToplaylist(song_name))
        menu.tk_popup(x_root, y_root)

    elif str(listbox.get(0)).find("Songs of playlist") > -1:
        playlist_name = str(listbox.get(0)).split(" ")[4:]
        playlist_name = " ".join(playlist_name)
        song_name = listbox.get(listbox.curselection())
        song_name = song_name[2:]
        menu = tk.Menu(tearoff=0)
        menu.add_command(label="remove song", command=lambda: removeSong(playlist_name, song_name))
        menu.tk_popup(x_root, y_root)


def add_new_artist():
    addwindow = tk.Tk()
    addwindow.title("Add new artist")
    addwindow.geometry('250x90')
    addwindow.configure(bg="black")
    lbl1 = tk.Label(addwindow, text="Name: ", fg="white", bg="black").grid(row=0, column=0)
    lbl2 = tk.Label(addwindow, text="birthday", fg="white", bg="black").grid(row=1, column=0)
    namebox = tk.Entry(addwindow)
    bdbox = tk.Entry(addwindow)
    namebox.grid(row=0, column=1)
    bdbox.grid(row=1, column=1)
    namebox.focus()
    artist = Artist()
    savebutton = tk.Button(addwindow, text="Add Artist", fg="white", bg="black",
                           command=lambda: artist.save(namebox.get(), bdbox.get()))
    savebutton.grid(row=2, column=1, padx=10, pady=5)

    addwindow.mainloop()


def add_new_album():
    addwindow = tk.Tk()
    addwindow.title("Add new album")
    addwindow.geometry('250x90')
    addwindow.configure(bg="black")
    lbl1 = tk.Label(addwindow, text="Title: ", fg="white", bg="black").grid(row=0, column=0)
    lbl2 = tk.Label(addwindow, text="songs_no: ", fg="white", bg="black").grid(row=1, column=0)
    title = tk.Entry(addwindow)
    songs_no = tk.Entry(addwindow)
    title.grid(row=0, column=1)
    songs_no.grid(row=1, column=1)
    title.focus()
    album = Album()
    savebutton = tk.Button(addwindow, text="Add Album", fg="white", bg="black",
                           command=lambda: album.save(title.get(), songs_no.get()))
    savebutton.grid(row=2, column=1, padx=10, pady=5)

    addwindow.mainloop()


root = tk.Tk()
root.title("Musicaly")
root.minsize(800, 520)
root.maxsize(800, 520)
root.configure(bg="black")

leftFrame = tk.Frame(root, bg="black", height=600, width=25)
leftFrame.grid(row=0, column=0, sticky="n")

button1 = tk.Button(leftFrame, text="Songs", fg="white", bg="Black", width=20, command=lambda: song(listbox))
button2 = tk.Button(leftFrame, text="Albums", fg="white", bg="Black", width=20, command=lambda: album(listbox))
button3 = tk.Button(leftFrame, text="playlists", fg="white", bg="Black", width=20,
                    command=lambda: playlist(listbox))
button4 = tk.Button(leftFrame, text="Artists", fg="white", bg="Black", width=20,
                    command=lambda: artist(listbox))
button5 = tk.Button(leftFrame, text="Bands", fg="white", bg="Black", width=20, command=lambda: band(listbox))
button6 = tk.Button(leftFrame, text="genre", fg="white", bg="Black", width=20, command=lambda: genre(listbox))
button7 = tk.Button(leftFrame, text="Add playlist", fg="white", bg="Black", width=20, command=lambda: addPlaylist())
button8 = tk.Button(leftFrame, text="Add New Artist", fg="white", bg="Black", width=20,
                    command=add_new_artist)
button9 = tk.Button(leftFrame, text="Add New Album", fg="white", bg="Black", width=20,
                    command=add_new_album)

button1.grid(row=0, padx=10, pady=5)
button2.grid(row=1, padx=10, pady=5)
button3.grid(row=2, padx=10, pady=5)
button4.grid(row=3, padx=10, pady=5)
button5.grid(row=4, padx=10, pady=5)
button6.grid(row=5, padx=10, pady=5)
button7.grid(row=6, padx=10, pady=5)
button8.grid(row=7, padx=10, pady=5)
button9.grid(row=8, padx=10, pady=5)

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
listbox.bind('<Double-1>', lambda x: doubleclick(listbox))
listbox.bind('<Button-3>', lambda e: popmenu(listbox, e.x_root, e.y_root))

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
# # directory = "/home/shehabeldeen/materials/concepts of programming/Musicaly/songs"
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
#         lyrics = ""
#         try:
#             text = urllib.request.urlopen(url)
#             lyrics = text.read()
#         except:
#             text = ""
#             pass
#
#         lyrics = str(lyrics)
#         where_start = lyrics.find('<!-- Usage of azlyrics.com content by any third-party')
#         start = where_start + 130
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
#         sng.save(name=title, release_date=audio.tag.release_date, lyrics=lyrics, length=audio.info.time_secs, path=path)
