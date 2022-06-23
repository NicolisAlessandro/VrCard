import sqlite3

def descrizioneBot(parametro):
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()   
    
    query_par = f'SELECT name_id FROM sites_info WHERE category_it == "Chiese"'    
    
    c.execute(query_par)
    data = c.fetchall()
    #for row in data:
     #   print(row)
    return data

def AffluenzaBot():
    conn = sqlite3.connect('bruh.db')
    c = conn.cursor()   
    
    query_par = f'SELECT data_visita FROM bruh'    
    
    c.execute(query_par)
    data = c.fetchall()
    for row in data:
        print(row)
    return row

#AffluenzaBot("Chiese")

def posizioneBot(parametro):
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()   
    
    query_par = f'SELECT longitude, latitude FROM sites_info WHERE category_it == "Chiese"'    
    
    c.execute(query_par)
    data = c.fetchall()

    for row in data:
        print(row)  
    return data

def descrizioneBot(parametro):
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()   
    
    query_par = f'SELECT name_id FROM sites_info WHERE category_it == "Monumenti"'    
    
    c.execute(query_par)
    data = c.fetchall()
    #for row in data:
     #   print(row)
    return data

def AffluenzaBot():
    conn = sqlite3.connect('bruh.db')
    c = conn.cursor()   
    
    query_par = f'SELECT data_visita FROM bruh'    
    
    c.execute(query_par)
    data = c.fetchall()
    for row in data:
        print(row)
    return row

#AffluenzaBot("Chiese")

def posizioneBot(parametro):
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()   
    
    query_par = f'SELECT longitude, latitude FROM sites_info WHERE category_it == "Monumenti"'    
    
    c.execute(query_par)
    data = c.fetchall()

    for row in data:
        print(row)  
    return data

#posizioneBot("Monumenti")