import sqlite3
          
print(list)

def descrizioneBot():
    conn = sqlite3.connect('veronacard.db')
    c = conn.cursor()   
    list = []
    Dup = []
    
    i2014=0
    i2015=0
    i2016=0
    i2017=0
    i2018=0
    i2019=0
    i2020=0
    
    query_par = f'SELECT sito_nome, data_visita FROM frequenza WHERE sito_nome == "Museo Miniscalchi Erizzo"'    
    
    c.execute(query_par)
    data = c.fetchall()
    for row in data:
        
        if  row in list:
            Dup.append(row)
            print (row)
            if "2020" in row[1] : 
                i2020 = i2020 + 1
            elif "2019" in row[1] : 
                i2019 = i2019 + 1
            elif "2018" in row[1] : 
                i2018 = i2018 + 1
            elif "2017" in row[1] : 
                i2017 = i2017 + 1
            elif "2016" in row[1] : 
                i2016 = i2016 + 1
            elif "2015" in row[1] : 
                i2015 = i2015 + 1
            elif "2014" in row[1] : 
                i2014 = i2014 + 1
        else:
            list.append(row)
            if "2020" in row[1] :
                i2020 = i2020 + 1
            elif "2019" in row[1] : 
                i2019 = i2019 + 1
            elif "2018" in row[1] : 
                i2018 = i2018 + 1
            elif "2017" in row[1] : 
                i2017 = i2017 + 1
            elif "2016" in row[1] : 
                i2016 = i2016 + 1
            elif "2015" in row[1] : 
                i2015 = i2015 + 1
            elif "2014" in row[1] : 
                i2014 = i2014 + 1
                
    print("2014 " + str(i2014))
    print("2015 " + str(i2015))
    print("2016 " + str(i2016))
    print("2017 " + str(i2017))
    print("2018 " + str(i2018))
    print("2019 " + str(i2019))
    print("2020 " + str(i2020))
    
    print(list)
            
    return data  

descrizioneBot()

#Complesso del Duomo
#2014 32112
#2015 32611
#2016 30963
#2017 35157
#2018 37044
#2019 34280
#2020 3126
#
#Chiesa di San Fermo
#2014 15108
#2015 14259
#2016 13743
#2017 14451
#2018 16235
#2019 15120
#2020 1399
#
#Torre dei Lamberti
#2014 46386
#2015 43695
#2016 46338
#2017 52688
#2018 51522
#2019 47777
#2020 2732

#Museo Africano
#2014 42
#2015 18
#2016 0
#2017 0
#2018 0
#2019 0
#2020 0

#Arena Museo Opera
#2014 548
#2015 0
#2016 0
#2017 0
#2018 0
#2019 0
#2020 0

#Museo degli Affreschi G.B. Cavalcaselle alla Tomba di Giulietta
#2014 17780
#2015 17773
#2016 16513
#2017 17787
#2018 15477
#2019 13943
#2020 1428

#Centro Internazionale di Fotografia Scavi Scaligeri
#2014 4508
#2015 540
#2016 0
#2017 0
#2018 0
#2019 0
#2020 0

#Museo Conte
#2014 0
#2015 705
#2016 554
#2017 13
#2018 0
#2019 0
#2020 0

#Museo della Radio
#2014 365
#2015 506
#2016 348
#2017 505
#2018 199
#2019 0
#2020 0

#Museo Miniscalchi Erizzo
#2014 106
#2015 38
#2016 85
#2017 34
#2018 88
#2019 119
#2020 13