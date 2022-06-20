import sqlite3

conn = sqlite3.connect('veronacard.db')
c = conn.cursor()

c.execute('SELECT name_id FROM sites_info')
for row in c.fetchall():
    print(row)
