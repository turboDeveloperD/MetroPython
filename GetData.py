#el chido
import csv
import DataCSV
import numpy as np
from classDistribution import Binomial
from classDistribution import geometrica
from classDistribution import Poisson
import matplotlib.pyplot as plt
import Partition

class GetData:
    #attributes
    listDataCSV = []
    listPartition = []
    tam = 18
    fileName = "afluenciastc_desglosado_02_2022.csv"
    
    #constructor
    def __init__(self):
        with open(self.fileName, "r", encoding="ISO-8859-1") as file:
            reader = csv.reader(file)
            i = 1
            for row in reader:
                if( i != 1):
                    station = row[5].encode('utf-8')
                    station = station.decode()
                    #afluenciaT = float(row[9]) # afluencia total
                    suma = float(float(row[6])+float(row[7])+float(row[8]))
                    ##objData = DataCSV.DataCSV(row[0], row[1], row[2], row[3], row[4], station, row[6], row[7], row[8], suma)
                    objetBinomial = Binomial.Binomial(18)
                    b = objetBinomial.generateBinomialDis()
                    bModal = objetBinomial.generateBimodalBino()
                    objetGeo = geometrica.Geometrica(self.tam)
                    g = objetGeo.generateGeometricaDis()
                    gModal = objetGeo.generateBimodalGeo()
                    objetPoisson = Poisson.Poisson(self.tam)
                    p = objetPoisson.generatePoissonDis()
                    pModal = objetPoisson.generateBimodalPos()
                    
                    
                    itemPartition = Partition.Partition(i,station, row[9], self.tam, b, g, p, bModal, gModal, pModal)
                    #itemPartition.generateData()
                    #self.listDataCSV.append(objData)
                    self.listPartition.append(itemPartition)
                    #(i, station, row[9], self.tam, b, g, p)
                i = i + 1
                
    
    #Method
    def createPartitions(self):
        for i in self.listDataCSV:
            print(i.StationInfo())

objTest = GetData()
#objTest.createPartitions()
#print("size listDataCSV: ",len(objTest.listDataCSV))
#item = 82679
#item = 10000
#item =2
item = 24520


print("size listPartition: ",len(objTest.listPartition))
print("Get item of listPartion TAM:", objTest.listPartition[item].tam)
print("Item: ", item)
print("total: ", objTest.listPartition[item].total)
print("Array Porcenb", objTest.listPartition[item].binoB)
print("Array Porceng", objTest.listPartition[item].binoG)
print("Array Porcenp", objTest.listPartition[item].binoP)

objTest.listPartition[item].generateData()

# graficas normales
x = np.arange(0, 18)
#plt.plot(x, objTest.listPartition[2].arrayHourB, '-o', label='Binomial')
#plt.plot(x, objTest.listPartition[2].arrayHourG, '-', label='Geometrica')
#plt.plot(x, objTest.listPartition[2].arrayHourP, '-.', label='Poisson')

print("Arrays")
print("Binomial", objTest.listPartition[item].arrayBimoB)
print("Geometrica", objTest.listPartition[item].arrayBimoG)
print("Poisson", objTest.listPartition[item].arrayBimoP)

# graficas Bimodals
plt.plot(x, objTest.listPartition[item].arrayBimoB, '-o', label='Binomial')
plt.plot(x, objTest.listPartition[item].arrayBimoG, '-', label='Geometrica')
plt.plot(x, objTest.listPartition[item].arrayBimoP, '-.', label='Poisson')

"""plt.plot(x, objTest.listPartition[2].arrayHourB, label='Binomial')
plt.plot(x, objTest.listPartition[2].arrayHourG, label='Geometrica')
plt.plot(x, objTest.listPartition[2].arrayHourP, label='Poisson')"""



plt.xlabel('Number of Events', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.title("Distribution Bimodals")
plt.legend()

plt.show()
            