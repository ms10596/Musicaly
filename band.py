import sqlite3


class Band:
    def __init__(self, id):
        self.id = id
        self.name = None

    def load(self, id):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Band where id =? """, (id,))
        result = s.fetchall()
        if len(result) == 0:
            return "not found"
        self.name = result[0][1]

    def save(self, name=""):
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Band VALUES(?, ?)""", (self.id, name))
        conn.commit()

    def __str__(self):
        return self.name

    def get_songs(self):
        from song import Song
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT id FROM Song where artist_id ={} OR ft_id={}""".format(self.id, self.id))
        songs_id = s.fetchall()
        songs = []
        for i in songs_id:
            new_song = Song(i[0])
            new_song.load()
            songs.append(new_song)
        return songs


if __name__ == '__main__':
    x = Band(0)
    # x.save("mshro3")
    x.load()
    print(x)