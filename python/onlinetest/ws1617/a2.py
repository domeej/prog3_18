'''
Created on 10.02.2019

@author: domee
'''


def konsonanten(s):
    for c in s:
        if c.upper() not in "AEIOU":
            yield c

def zahlen(n):
    while(1):
        for e in range(n+1):
            yield e

def mal123(g):
    for e in list(g):
        if e % 2 == 0:
            yield e
            yield e
        if e % 2 != 0:
            yield e
            yield e
            yield e


def kleinersum(g):
    sum = '#'
    for e in g:
        if sum == '#':
            sum = e
        if e < sum:
            yield e    
        sum += e
        
        
def produkt(g):
    prod = 1
    for e in g:
        prod = prod * e
        yield prod
        
def zahlwoerter(g):
    for e in g:
        if e == 0:
            yield 0
        
        if type(e) == int:
            if e == 1:
                yield "eins"
            if e == 2:
                yield "zwei"
            if e == 3:
                yield "drei"
        else:
            yield e
        
if __name__ == '__main__':
    lis = []
    
    x = zahlen(5)
    for e in range(16):
        lis.append(next(x))
    print(lis)
    
    lis = ""
    for e in konsonanten("Hallo schoene Welt!"):
        lis += e
    print(lis)
    
    print(list(mal123([1,2,3,4,5])))
    print(list(kleinersum(iter([1,2,4,6,8,22,30]))))
    print(list(produkt([1,2,3,4,6,7,8])))
    print(list(zahlwoerter(["Ein", "mal", "1", "ist", "keins", "und", 2, "und 2", "und", 4,3,2,1,0])))
    
    
    
    