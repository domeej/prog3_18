FILENAME = 'messwerte.csv'    

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

def method1():
    f = open(FILENAME, 'r')
    for line in f:
        x = Messwert(line)
        print(x) 

def method2():
    f = open(FILENAME, 'r')
    for line in f:
        zeitpunkt, temperatur = getInformation(line)
        x = Messwert(zeitpunkt,temperatur)
    
        
def checkEquality():
    f = open(FILENAME)
    for line in f:
        x = Messwert(line)
        print(eval(repr(x)) == x)
    
def checkLessThan():
    a = Messwert("2013-07-15 18:45:01.420677",20.375)
    b = Messwert("2013-07-15 19:00:01.885987",19.5625)
    c = Messwert("2013-07-15 19:00:01.885987",19.5625)
    d = Messwert("2014-07-15 19:00:01.885987",23.5625)
    e = Messwert("2014-07-15 19:00:07.885987",19.5625)
    f = Messwert("2014-07-15 19:00:07.885987",15.5625)
    
    #Set tests geht weil __hash__
    x = {a,b,c,e,f,f}
    
    s = set()
    s.add(a)
    s.add(b)
    s.add(c)
    print(x)
    print(s)
    
    # sorting tests geht weil __eq__ und __lt__
    lis = [c,d,f,a,b,e]
    print(sorted(lis))
    
    # tests auf < > == 
    print(b==a)
    print(a<b)
    
if  __name__ =='__main__':
    #method2()
    #method1()
    #checkEquality()
    checkLessThan()
    
    