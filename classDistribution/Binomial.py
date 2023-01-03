import numpy as np
import scipy.stats as stats
#import matplotlib.pyplot as plt

class Binomial:
    
    # Atributos
    arrayB = []
    arrayBimodalB = []
    tam    = 0
    
    def __init__(self, _tam):
        self.tam = _tam
    
    def generateBinomialDis(self):
        x = np.arange(0, self.tam)
        b = stats.binom.pmf(x, self.tam, 0.1*3)
        self.arrayB = b
        return self.arrayB
    
    def generateBimodalBino(self):
        x = np.arange(0, (self.tam/2))
        #binom1 = stats.binom.pmf(x, 18, 0.1*6)
        #binom2 = stats.binom.pmf(x, 18, 0.1*9)
        
        binom1 = stats.binom.pmf(x, 18, 0.1*2)
        binom2 = stats.binom.pmf(x, 18, 0.1*9)
        #print(binom1)
        #print(binom2)
        self.arrayBimodalB = np.concatenate([binom1, binom2])
        #print(self.arrayBimodalB)
        
        return self.arrayBimodalB
    
    def imprimirArray(self):
        print(self.arrayB)
        

"""b1 = Binomial(18)
b1.generateBimodalBino()
x = np.arange(0, 18)"""
"""plt.plot(x, b1.arrayBimodalB, '-o')
plt.xlabel('Number of Events', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.title("Binomial Distribution varying λ")
plt.show()"""
#b1.generateBinomialDis()
#b1.imprimirArray()



    
        