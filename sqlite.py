import sqlite3

# con = sqlite3.connect("db.sqlite")
con = sqlite3.connect(":memory:")
con.text_factory = str

cur = con.cursor()

file = open("schema.sql", "r", encoding="utf-8")
while True:
    line = file.readline()
    if not line: break
    print(line)
    cur.execute(line)
file.close()

file = open("data.sql", "r", encoding="utf-8")
while True:
    line = file.readline()
    if not line: break
    print(line)
    cur.execute(line)
file.close()

con.close()
