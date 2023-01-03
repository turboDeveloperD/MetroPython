import csv
import DataCSV

listDataCSV = []

with open("afluenciastc_desglosado_02_2022.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        #obj = DataCSV.DataCSV(row[0].encode('utf-8'), row[1], row[2].encode('utf-8'), row[3], row[4].encode('utf-8'), row[5].encode('utf-8'), row[6], row[7], row[8], row[9])
        station = row[5].encode('utf-8')
        station = station.decode()
        obj = DataCSV.DataCSV(row[0], row[1], row[2], row[3], row[4], station, row[6], row[7], row[8], row[9])
        #obj.StationInfo()
        listDataCSV.append(obj)
        """print(row[0].decode('utf-8'))
        print(row[1])
        print(row[2].decode('utf-8'))
        print(row[3])
        print(row[4].decode('utf-8'))
        print(row[5].decode('utf-8'))
        print(row[6])
        print(row[7])
        print(row[8])
        print(row[9])""
        #list.append( Partition(row[0].encode('utf-8'), row[1], row[2].encode('utf-8'), row[3], row[4].encode('utf-8'), row[5].encode('utf-8'), row[6], row[7], row[8], row[9]) )"""

for value in listDataCSV:
    print(value.StationInfo())
    
#print(len(listDataCSV))
