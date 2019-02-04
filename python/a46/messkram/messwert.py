'''
Created on 03.02.2019

@author: domee
'''

class Messwert:
    def __init__(self, *data):
        if len(data) == 1:
            self.zeitpunkt, self.temperatur = getInformation("".join(data))
            self.temperatur = float(self.temperatur)
            
        if len(data) == 2:
            self.zeitpunkt = data[0]
            self.temperatur = float(data[1])
            
    def __eq__(self, other):
        return self.zeitpunkt == other.zeitpunkt and self.temperatur == other.temperatur 
        
    def __str__(self):
        return self.zeitpunkt+ ","  + str(self.temperatur)

    def __repr__(self):
        return 'Messwert('+ self.zeitpunkt + ',' + str(self.temperatur) + ')'
    

    def __lt__(self,other):
        if self.zeitpunkt == other.zeitpunkt:
            return self.temperatur < other.temperatur
        
        return self.zeitpunkt < other.zeitpunkt
    
    def __hash__(self):
        return hash((self.temperatur, self.zeitpunkt))
    
    
def getInformation(line):
    line = line.split(',')
    zeitpunkt  = line[0]
    temperatur = line[1].rstrip()
    return (zeitpunkt,temperatur)
