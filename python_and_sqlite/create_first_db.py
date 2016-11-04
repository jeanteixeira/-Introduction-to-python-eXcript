import sqlite3

path = r'/home/jean/Introduction-to-python-eXcript/python_and_sqlite'
conn = sqlite3.connect(path+r'/teste.db')

cursor = conn.execute('select * from contatos')
rows = cursor.fetchall()

for row in rows:
	print(row)

