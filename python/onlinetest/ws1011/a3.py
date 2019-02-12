'''
Created on 12.02.2019

@author: dkoeh001
'''

def nmischen(g1 ,n ,g2):
    
    while(True):
        for e in range(n):
            yield next(g1)
        yield next(g2)


def vielfach(g1, n):
    i = 0
    for e in g1:
        while(i<n): 
            i+=1
            yield e
        i = 0
        
def getestet(g1, test):
    for e in g1:
        if test(e):
            yield e


def test(w):
    return w % 2 == 0

def gen1():
    while(True):
        for e in range(10):
            yield e
    
def gen2():
    while(True):
        for e in list(range(1000)[::100]):
            yield e



if __name__ == '__main__':
    g1 = [0,1,2,3,4,5,6,7,8,9,10]
    g2 = [100,200,300,400,500,600]
    
    #for e in vielfach(g1,3):
    #    print(e)
    #print(test(3))
    a = gen1()
    b = gen2()
    
    
    print([e for e in getestet(g1, test)])
    
    for e in nmischen(a,2,b):
        print(e)
    
   
        