import numpy as np
import scipy.stats as stats
#import matplotlib.pyplot as plt


class Geometrica:
    
    #atributos
    arrayG = []
    arrayBimodalG = []
    tam    = 0
    
    def __init__(self, _tam):
        self.tam = _tam
    
    def generateGeometricaDis(self):
        x = np.arange(0, self.tam)
        g = stats.geom.pmf(x, 0.18)
        self.arrayG = g
        return self.arrayG
    
    def generateBimodalGeo(self):
        x = np.arange(0, (self.tam/2))
        #geo1 = stats.geom.pmf(x,0.06)
        #geo2 = stats.geom.pmf(x,0.06*2)
        geo1 = stats.geom.pmf(x,0.06*2)
        geo2 = stats.geom.pmf(x,0.06*4)
        #print(geo1)
        #print(geo2)
        self.arrayBimodalG = np.concatenate([geo1, geo2])
        #print(self.arrayBimodalG)
        return self.arrayBimodalG
        
        

    def imprimirArray(self):
        print(self.arrayG)


#g = Geometrica(18)
"""g.generateGeometricaDis()
g.imprimirArray()"""
"""g.generateBimodalGeo()
x = np.arange(0, 18)
plt.plot(x, g.arrayBimodalG, '-o')
plt.ylabel("Probability", fontsize="18")
plt.xlabel("X - No. of Throws", fontsize="18")
plt.title("Geometric Distribution - No. of Throws Vs Probability", fontsize="18")
plt.show()"""
