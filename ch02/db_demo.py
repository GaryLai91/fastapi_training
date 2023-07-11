import sqlite3

path = "inventory.db"
conn = sqlite3.connect(path, check_same_thread=False)
cur = conn.cursor()

sql = "select * from items"
items = cur.execute(sql)
for item in items:
    print(item)

cur.close()
conn.close()