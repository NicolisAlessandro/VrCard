import sqlite3




def read_from_db():
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()
    c.execute('SELECT latitude, longitude FROM sites_info')
    data = c.fetchall()
    for row in data:
        print(row)
        
#read_from_db()

def descrizioneBot(parametro):
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()   
    
    query_par = f'SELECT name_id FROM sites_info WHERE category_it == "Chiese"'    
    
    c.execute(query_par)
    data = c.fetchall()
    #print("dati:", data)
    #print("tipo: ", type(data))
    for row in data:
        print(row)

descrizioneBot("Chiese")
        
        
def creaBottonibot(parametro):
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()      
    query_par = f'SELECT name_id  FROM sites_info WHERE category_it == "{parametro}" '   
    c.execute(query_par)
    