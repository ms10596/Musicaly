import sqlite3


class Band:
    def __init__(self, id):
        self.id = id
        self.name = None

    def load(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Band where id ={} """.format(self.id))
        result = s.fetchall()
        self.name = result[0][1]

    def save(self, name=""):
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Band VALUES(?, ?)""", (self.id, name))
        conn.commit()

    def __str__(self):
        return self.name


if __name__ == '__main__':
    x = Band(0)
    # x.save("mshro3")
    x.load()
    print(x)
