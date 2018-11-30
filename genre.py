import sqlite3


class Genre:
    def __init__(self, id):
        self.id = id
        self.name = None

    def load(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Genre where id ={} """.format(self.id))
        result = s.fetchall()
        self.name = result[0][1]

    def save(self, name):
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Genre VALUES(?, ?)""", (self.id, name))
        conn.commit()

    def __str__(self):
        return self.name


if __name__ == '__main__':
    g2 = Genre(2)
    g2.save("arabic")
