import sqlite3


class Artist:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.dob = None

    def load(self):
        conn = sqlite3.connect('db/musicaly.db')
        s = conn.execute("""SELECT * FROM Artist where id ={} """.format(self.id))
        result = s.fetchall()
        print(result)
        if len(result) == 0:
            return "not found"
        self.name = result[0][1]
        self.dob = result[0][2]
        conn.close()

    def save(self, name="", dob="", band_id=""):
        conn = sqlite3.connect('db/musicaly.db')
        conn.execute("""INSERT INTO Artist VALUES(?, ?, ?)""", (name, dob, band_id))
        conn.commit()
        conn.close()

    def __str__(self):
        return str(self.name) + " " + str(self.dob)


if __name__ == '__main__':
    a0 = Artist(0)
    print(a0.load())
    print(a0)
    # a0.save("dua lipa", "22/8/1995")
    # print(a0)
