import sqlite3


class Playlist:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.description = None
        self.playlist_song_id = None

    def load(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Playlist where id ={} """.format(self.id))
        result = s.fetchall()
        self.name = result[1]
        self.description = result[2]
        self.playlist_song_id = result[3]

    def save(self, name="", describtion="", playlist_song_id=""):
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Playlist VALUES(?, ?, ?, ?)""", (self.id, name, describtion, playlist_song_id))
        conn.commit()


if __name__ == '__main__':
    x = Playlist(0)
    # x.save("sad")
    x.load()
