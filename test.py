import csv
list = []
Dup = []
with open('veronacard_2014_opendata.csv', newline='', encoding="ISO-8859-1") as filecsv:
    reader = csv.reader(filecsv)
    for row in reader:
        #print(row[5])
        if  row[5] in list:
            Dup.append(row[5])
        else:
            list.append(row[5])
            
print(list)       