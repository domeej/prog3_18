from collections.abc import Iterable
from messwert import Messwert

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
        