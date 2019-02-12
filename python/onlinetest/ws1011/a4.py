'''
Created on 12.02.2019

@author: dkoeh001
'''
from _pytest.compat import isfunction
from pylint.test.functional.bad_whitespace import function

def add1(x): 
    return x+1
def mul2(x): 
    return x*2

def hintereinander(*funcs):
    
    def fun(x):
        
        
        pass
        
    
    
        
    
def partiell(func, *args):
    pass




if __name__ == '__main__':
    
    g = hintereinander(add1, mul2)
    print(g(3))