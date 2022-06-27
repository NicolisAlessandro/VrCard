
#
#  file: letturaDb
#  authors: Alessandro, Simone , Michela
#  date: 27/06/2022
#  description: read of the database sqlite3
#

import sqlite3
import math

def descrizioneBot(parametro):
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()   
    
    query_par = f'SELECT descr_it FROM sites_info WHERE category_it == "Chiese"'    
    
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

#def posizioneBot(parametro):
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
    
    query_par = f'SELECT name_id, descr_it, address FROM sites_info WHERE category_it == "Monumenti"'    
    
    c.execute(query_par)
    data = c.fetchall()

    #for row in data:
    #    print(row) 
    
    return data

descrizioneBot("Chiese")

def AffluenzaBot():
    conn = sqlite3.connect('bruh.db')
    c = conn.cursor()   
    
    query_par = f'SELECT data_visita FROM bruh'    
    
    c.execute(query_par)
    data = c.fetchall()
    #for row in data:
    #    print(row)
    return data

#AffluenzaBot("Chiese")

def posizioneBoty(parametro):
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()   
    
    query_par = f'SELECT longitude FROM sites_info WHERE category_it == "Monumenti"'    
    
    c.execute(query_par)
    data = c.fetchall()
    print (data[2])
    #for row in data:
    #    print(row)  
    return data

posizioneBoty("Monumenti")

def posizioneBotx(parametro):
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()   
    
    query_par = f'SELECT latitude FROM sites_info WHERE category_it == "Monumenti"'    
    
    c.execute(query_par)
    data = c.fetchall()
    
    print (data[2])
    #for row in data:
    #    print(row)  
    return data

posizioneBotx("Monumenti")

#def reply_location(paramtero):
    #conn = sqlite3.connect('veronacard.db')
    #c = conn.cursor()   
    
    #query_par = f'SELECT longitude, latitude FROM sites_info WHERE category_it == "Monumenti"'
    
    #c.execute(query_par)
    #data = c.fetchall()
    
    #Ox=0.0; Oy=0.0
    #Ax=3.0; Ay=4.0
    #Bx=4.0; By=3.0
 
    #dOA=math.sqrt((Ox-Ax)**2 + (Oy-Ay)**2)
    #dOB=math.sqrt((Ox-Bx)**2 + (Oy-By)**2)
    #dAB=math.sqrt((Ax-Bx)**2 + (Ay-By)**2)
 
    #print("OA =",dOA)
    #print("OB =",dOB)
    #print("AB =",dAB)
    
    #for row in data:
        #print(row)  
    #return data

#reply_location("paramtero")

