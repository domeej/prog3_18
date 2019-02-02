import sys
from plist import Integer
import string
sys.path.insert(0, '/home/domee/gitRepos/prog3_18/python/a39')
from a39 import Messwert

#import a39.a39
'''
Created on 29.01.2019

@author: domee
'''
from _collections_abc import Iterable
FILENAME = "messwerte.csv"

class Test:
    def __init__(self):
        self.menge = {1,2,3}

        
    def add(self,other):
        self.menge.add(other)
        
        
    def __add__(self,other):
        self.add(other)

class Messreihe:
    
    def __init__(self, data=None):
        self.menge = []
        if isinstance(data, Iterable):
            for line in data:
                m = Messwert(line)
                if m not in self.menge:
                    self.menge.append(m)
                
    def __len__(self):
        return len(self.menge)
    
    def add(self, *messwerte):
        if len(messwerte) == 1 and isinstance(*messwerte, Messwert):
            if messwerte not in self.menge:
                self.menge.append(messwerte)
        elif len(messwerte) > 1 :
            for messwert in messwerte:
                if messwert not in self.menge:
                    self.menge.append(messwert)
        else:
            raise TypeError
    
    def __add__(self, other):
        if(isinstance(other, Messwert)):
            self.add(other)
            return self.menge
        if isinstance(other, tuple):
            self.add(other[0])
        else:
            raise TypeError    
        
    def __radd__(self, other):
        return self.__add__(other)
    
    def __iter__(self):
        self.pos = -1
        return self
    
    def __next__(self):
        self.pos +=1
        self.menge = sorted(self.menge)
        if self.pos >= len(self.menge):
            raise StopIteration
        return self.menge[self.pos]
    
    def __getitem__(self, i):
        if isinstance(i, int):
            self.menge = sorted(self.menge)
            return self.menge[i]
        if isinstance(i, str):
            new = Messreihe()
            for messwert in self.menge:
                if i in messwert[0].zeitpunkt:
                    new + messwert
            return new
                  
    def __setitem(self, i, value):
        self.menge = sorted(self.menge)
        self.menge[i] = value
    
    
if __name__ == '__main__':
    #x= Messreihe(open(FILENAME, 'r'))
    x = Messreihe()
    print(type(x))
    x + Messwert("2013-07-15 16:03:08.260597",19.875)
    x + Messwert("2013-07-16 18:03:08.260597",22.875)
    x + Messwert("2013-07-16 18:03:08.260597",22.875)
    x + Messwert("2013-07-16 18:03:08.260597",24.875)
    x + Messwert("2013-07-16 18:03:08.260597",18.875)
    #x.add("yow")
    x + Messwert("2018-07-16 18:03:08.260597",1.875)

    print(x.menge[2])
    print(len(x))
    

    print(type(x))
    for e in x:
        print("x:",e)
    
    print(x[3])
    a = x['2013-07-16 18:03']
    print(a)
    print(a.menge)
    print("slicing:", a.menge[-1:])
    print(x)
    print(x.menge)
    
         
         
    
    