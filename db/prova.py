import sqlite3
import time
import datetime



conn = sqlite3.connect('veronacard.db')
c = conn.cursor()

def read_from_db():
    c.execute('SELECT latitude, longitude FROM sites_info')
    data = c.fetchall()
    for row in data:
        print(row)
        
read_from_db()