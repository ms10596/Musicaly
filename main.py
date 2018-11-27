import sqlite3
import os
from tkinter import *
import pygame
import eyed3
from tkinter.filedialog import askdirectory


qry = open("db/musicaly.sql").read()
conn = sqlite3.connect('db/musicaly.db')
conn.executescript(qry)

directory = askdirectory()
os.chdir(directory)

for files in os.listdir(directory):
    if files.endswith(".mp3"):
        realdir = os.path.realpath(files)
        audio = eyed3.load(realdir)
        print(audio.tag.artist)

