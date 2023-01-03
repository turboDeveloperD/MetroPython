class Partition:
    #attributions
    id = 0
    stationName = ''
    total = 0.0
    tam = 0.
    porcB = []
    porcG = []
    porcP = []
    arrayHourB = []
    arrayHourG = []
    arrayHourP = []
    binoB     = []
    binoG     = []
    binoP     = []
    arrayBimoB = []
    arrayBimoG = []
    arrayBimoP = []

    def __init__(self, _id, _stationName, _total, _tam, _porcB, _porcG, _porcP, _binoB, _binoG, _binoP):
        self.id          = _id
        self.stationName = _stationName
        self.total       = _total
        self.tam         = _tam
        self.porcB       = _porcB
        self.porcG       = _porcG
        self.porcP       = _porcP
        self.binoB       = _binoB
        self.binoG       = _binoG
        self.binoP       = _binoP
        
    
    def generateData(self):
        """for i, value in enumerate(self.porc):
              value = value * self.total
              self.arrayHour.append(value)"""
        self.generateArrayBino()
        self.generateArrayGeo()
        self.generateArrayPoisson()
        self.generateBimodalB()
        self.generateBimodalG()
        self.generateBimodalP()
        
        #for i in range(self.tam):
            #value = 
    
    def generateArrayBino(self):
        for i, value in enumerate(self.porcB):
            value = value * float(self.total)
            self.arrayHourB.append(value)
        
        #print("Binomial")
        #print(self.arrayHourB)
        return self.arrayHourB
        
    
    def generateArrayGeo(self):
        for i, value in enumerate(self.porcG):
            value = value * float(self.total)
            self.arrayHourG.append(value)
        
        #print("Geometrica")
        #print(self.arrayHourG)
        return self.arrayHourG
    
    def generateArrayPoisson(self):
        for i, value in enumerate(self.porcP):
            value = value * float(self.total)
            self.arrayHourP.append(value)
        
        #print("Poisson")
        #print(self.arrayHourP)
        return self.arrayHourP
    
    """
    Bimodals
    """
    def generateBimodalB(self):
        for i, value in enumerate(self.binoB):
            value = value * float(self.total)
            self.arrayBimoB.append(value)
        
        print("Bimodal Binomial")
        print(self.arrayBimoB)
        return self.arrayBimoB
    
    def generateBimodalG(self):
        for i, value in enumerate(self.binoG):
            value = value * float(self.total)
            self.arrayBimoG.append(value)
        
        print("Bimodal Geometric")
        print(self.arrayBimoG)
        return self.arrayBimoG
    
    def generateBimodalP(self):
        for i, value in enumerate(self.binoP):
            value = value * float(self.total)
            self.arrayBimoP.append(value)
        
        print("Bimodal Poisson")
        print(self.arrayBimoP)
        return self.arrayBimoP
    
    def getArrayBino(self):
        return self.arrayHourB        
    
    def getArrayGeo(self):
        return self.arrayHourG  

    def getArrayPoisson(self):
        return self.arrayHourP

"""myObj = Partition(1, 'New Station', 1853, 18, [1,5,2,6,4], [1,3,22,432,0], [1,0,5465,78,432])
myObj.generateData()

b = myObj.getArrayBino()
g = myObj.getArrayGeo()
p = myObj.getArrayPoisson()
print(b)
print(g)
print(p)"""



#myObj.getPartition()