import sys,os
from plist import Integer
sys.path.insert(0, '/home/domee/gitRepos/prog3_18/python/a39')
from a39 import Messwert

'''
Created on 29.01.2019

@author: domee
'''
from _collections_abc import Iterable
FILENAME = "messwerte.csv"

class MonotonieVerstossError(ValueError):
    def __init__(self):
        pass

class MessreiheEigenIter:
    def __init__(self, menge):
        self.menge = menge
        self.pos = -1

    def __iter(self):
        return self

    def __next__(self):
        self.pos += 1
        if self.pos >= len(self.menge):
            raise StopIteration
        
        return self.menge[self.pos]

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
    
    def addNew(self, mw):
        
        if mw.zeitpunkt > self.menge[len(self.menge)-1].zeitpunkt:
            self.add(mw)
        
        else:
            raise MonotonieVerstossError
    
    
    def add(self, *messwerte):
        if len(messwerte) == 1 and isinstance(messwerte[0], Messwert):
            mw  = messwerte[0]
            
            if mw not in self.menge:
                self.menge.append(mw)
        elif len(messwerte) > 1 :
            for messwert in messwerte:
                if messwert not in self.menge:
                    self.menge.append(messwert)
        else:
            raise TypeError("übergebene Werte sind keine Messwerte", *messwerte)
    
    def __add__(self, other):
        assert(isinstance(other, (Messwert,tuple))), "übergebener Wert ist kein Messwert11!!ELF"
        
        if(isinstance(other, Messwert)):
            self.add(other)
            return self.menge
        if isinstance(other, tuple):
            self.add(other[0])
        
    def __radd__(self, other):
        return self.__add__(other)
    
    def __iter__(self):
        
        #alternativ mit eigener Iteratorklasse:
        #return MessreiheEigenIter(self.menge)
        
        #alternativ mit eigener Generatorklasse:
        return self.erzeugeIterator()   
        
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
                if i in messwert.zeitpunkt:
                    new + messwert
            return new
                  
    def __setitem(self, i, value):
        self.menge = sorted(self.menge)
        self.menge[i] = value
        
    def erzeugeIterator(self):
        for m in self.menge:
            yield m

    
def enum(iterable):
    i = -1
    for e in iterable:
        i += 1
        yield i,e
        
  
if __name__ == '__main__':
    #x= Messreihe(open(FILENAME, 'r'))
    x = Messreihe()
    print(type(x))
    x + Messwert("2013-07-15 16:03:08.260597",19.875)
    x + Messwert("2013-07-16 18:03:08.260597",22.875)
    x + Messwert("2013-07-16 18:03:08.260597",22.875)
    x + Messwert("2013-07-16 18:03:08.260597",24.875)
    x + Messwert("2013-07-16 18:03:08.260597",18.875)
    x + Messwert("2018-07-16 18:03:08.260597",1.875)
    #x + ("Vogel")
    #x + ("Vogel", 'piep')

    print(x.menge[2])
    print(len(x))

    print(type(x))
    for i,e in enum(x):
        print(i,"x:",e)
    
    print(x[3])
    a = x['2013-07-16 18:03']
    print(a)
    print(a.menge)
    print("slicing:", a.menge[-1:])
    print(x)
    print(x.menge)
    
    x.addNew(Messwert("2018-07-16 18:03:07.260597",1.875))
         
    
    