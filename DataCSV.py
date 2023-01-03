class DataCSV:
    
    #atributos
    date = ''
    day = 0
    month = ''
    year = 0
    line = ''
    station = ''
    a_boleto = 0
    a_prepago = 0
    a_gratuidad = 0
    a_total = 0
    
    def __init__(self, _date, _day, _month, _year, _line, _station, _a_boleto, _a_prepago, _a_gratuidad, _a_total):
        self.date = _date
        self.day =_day
        self.month = _month
        self.year =_year
        self.line = _line
        self.station = _station
        self.a_boleto =_a_boleto
        self.a_prepago = _a_prepago
        self.a_gratuidad =_a_gratuidad
        self.a_total = _a_total
    
    def getDate(self):
        return self.date
    
    def getDay(self):
        return self.day
    
    def getMonth(self):
        return self.month
    
    def getYear(self):
        return self.year
    
    def getLine(self):
        return self.line
    
    def getStation(self):
        return self.station
    
    def getA_Boleto(self):
        return self.a_boleto
    
    def getA_Prepago(self):
        return self.a_prepago
    
    def getA_Gratitud(self):
        return self.a_gratuidad
    
    def getA_Total(self):
        return self.a_total
    
    def StationInfo(self):
        print("The data is: ", self.date, self.day, self.month, self.year, self.line, self.station, self.a_boleto, self.a_prepago, self.a_gratuidad, self.a_total)
        
"""p1 = DataCSV("2021-02-07", 7, "Febrero", 2021, "Linea 1","Isabel la Católica", 979, 1659, 0, 2638)
p1.StationInfo()"""