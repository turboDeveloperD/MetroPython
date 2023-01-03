import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

class Poisson:
    
    #attributions
    arrayP = []  # arreglo con la distribucion
    tam    = 0  # tamaño del arreglo
    arrayBimodalPoisson = []
    
    def __init__(self, _tam):
        self.tam = _tam
    
    def generatePoissonDis(self):
        x = np.arange(0, self.tam)
        poisson = stats.poisson.pmf(x, 2)
        self.arrayP = poisson
        return self.arrayP
    
    def generateBimodalPos(self):
        x = np.arange(0, (self.tam/2))
        #pos1 = stats.poisson.pmf(x, 4)
        #pos2 = stats.poisson.pmf(x, 6)
        
        pos1 = stats.poisson.pmf(x, 6)
        pos2 = stats.poisson.pmf(x, 9)
        #print(pos1)
        #print(pos2)
        self.arrayBimodalPoisson = np.concatenate([pos1,pos2])
        return self.arrayBimodalPoisson
        
        
    
    def imprimirArray(self):
        print(self.arrayP)
        

"""p1 = Poisson(18)
a = p1.generatePoissonDis()
print(a)
p1.generateBimodalPos()
x = np.arange(0, 18)
plt.plot(x, p1.arrayBimodalPoisson, '-o')
plt.xlabel('Number of Events', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.title("Poisson Distribution varying λ")
plt.show()"""

        
    