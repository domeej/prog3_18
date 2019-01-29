import sys
sys.path.insert(0, '/home/domee/gitRepos/prog3_18/python/a39')
from a39 import Messwert

#import a39.a39
'''
Created on 29.01.2019

@author: domee
'''
from _collections_abc import Iterable
FILENAME = "messwerte.csv"



class Messreihe:
    #self.menge = set()
    
    def __init__(self, data=None):
        self.menge = set()
        if isinstance(data, Iterable):
            for line in data:
                m = Messwert(line)
                self.menge.add(m)
                
    def __len__(self):
        return len(self.menge)
    

    
    def add(self, *messwerte):
        if len(messwerte) == 1 and isinstance(*messwerte, Messwert):
            self.menge.add(*messwerte)
        elif len(*messwerte) > 1:
            for messwert in messwerte:
                self.menge.add(messwert)
        else:
            raise TypeError
    
if __name__ == '__main__':
    x= Messreihe(open(FILENAME, 'r'))
    x = Messreihe()
    x.add(Messwert("2013-07-15 16:03:08.260597",19.875))
    print(len(x))
    

    print(x)
    