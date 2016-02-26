import sqlite3

conn = sqlite3.connect('babyorm.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Users")

c.execute("""CREATE TABLE Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    username VARCHAR,
    email VARCHAR,
    created_at DATE,
    updated_at DATE
)""")

conn.commit()








users = [
	["test", "testing", "testing@gmail.com"],
	["Jack", "Janteby", "Janteby@gmail.com"],
	["test2", "testing2", "testing2@gmail.com"]
]

length = len(users)
for user in users:
	c.execute(
	"""
	INSERT INTO Users ("name","username","email") VALUES(?,?,?)

	""",(user[0],user[1],user[2])
	)

	conn.commit()

conn.close()