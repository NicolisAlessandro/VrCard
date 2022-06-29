
#
#  file: letturaDb
#  authors: Alessandro, Simone , Michela
#  date: 27/06/2022
#  description: read of the database sqlite3
#

import sqlite3
import math

def NomeBot():
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()   
    
    query_par = 'SELECT name_id FROM sites_info'    
    
    c.execute(query_par)
    data = c.fetchall()
    return data

def descrizioneBot(parametro):
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()   
    
    query_par = f'SELECT name_id, descr_it, address FROM sites_info WHERE category_it == "{parametro}"'    
    
    c.execute(query_par)
    data = c.fetchall()
    return data

def descrizioneEngBot(parametro):
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()   
    
    query_par = f'SELECT name_id, descr_it, address FROM sites_info WHERE category_it == "{parametro}"'    
    
    c.execute(query_par)
    data = c.fetchall()   
    return data

def posizioneBoty(parametro):
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()   
    
    query_par = f'SELECT longitude FROM sites_info WHERE category_it == "{parametro}"'    
    
    c.execute(query_par)
    data = c.fetchall()
    print (data[2])
    return data

def posizioneBotx(parametro):
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()   
    
    query_par = f'SELECT latitude FROM sites_info WHERE category_it == "{parametro}"'    
    
    c.execute(query_par)
    data = c.fetchall()
    
    print (data[2])
    return data