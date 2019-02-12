'''
Created on 12.02.2019

@author: dkoeh001
'''


class Klasse(object):
    instanzen = 0
    def __init__(self, zahl1='#'):
        Klasse.instanzen += 1
        
        if type(zahl1) == int:
            self.zahl1 = zahl1
        else:
            self.zahl1 = zahl1
            
    def add(self, para1):
        if type(self.zahl1) == int:
            return self.zahl1+para1
        else:
            return para1
        
        
    @staticmethod
    def wieviel():
        return Klasse.instanzen

class Erbe(Klasse):
    def __init__(self, zahl1='#', zahl2='#'):
        Klasse.__init__(self, zahl1= zahl1)
        
        if type(zahl2) == int:
            self.zahl2 = zahl2
        else:
            self.zahl2 = zahl2
        print("zahl:",self.zahl2)
        
    def mul(self,para2):
        print(self.zahl2)
        if type(self.zahl2) == int:
            return self.zahl2 * para2
        else:
            return para2*3
        
    def __mul__(self, value):
        pass    
    
    
if __name__ == '__main__':
    pass

    a = Klasse()
    b = Klasse(4)
    print("instanzen:", Klasse.wieviel())
    print("add: ",b.add(2))
    
    c = Erbe()
    #print(c)
    print(c.instanzen)
    print(c.mul(3))
    
    
    
    