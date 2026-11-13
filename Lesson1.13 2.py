import sqlite3

connection = sqlite3.connect("shop.sl3")
cur = connection.cursor()
print("Підключення успішне")

cur.execute("CREATE TABLE IF NOT EXISTS fruits (name TEXT, price INTEGER)")

#cur.execute("INSERT INTO fruits (name, price) VALUES ('apples', 70)")
#cur.execute("INSERT INTO fruits (name, price) VALUES ('mangos', 120)")
#cur.execute("INSERT INTO fruits (name, price) VALUES ('bannanas', 80)")

connection.commit()

cur.execute("SELECT * FROM fruits")
print(cur.fetchall())

cur.execute("SELECT * FROM fruits WHERE price > 70")
print(cur.fetchall())

cur.execute("UPDATE fruits SET price = 150 WHERE name = 'mangos' ")
connection.commit()

cur.execute("SELECT * FROM fruits")
print(cur.fetchall())

cur.execute("DROP TABLE fruits")
connection.commit()

connection.close()

