'''
Created on 12.02.2019

@author: dkoeh001
'''
import sys


def mach(s):
    result = ""
    pre = '#'
    zaehler = 1
    
    for c in s:
        
        if pre == c:
            zaehler += 1
        else:
            if zaehler > 1:
                result +=  pre + str(zaehler)
            elif pre != '#':
                result += pre
            zaehler = 1
            pre = c
        
    result += pre
    if zaehler > 1:
        result += str(zaehler)

        
        
    print(result)
    
def komprimier():
    args = sys.argv[1:]
    
    for arg in args:
        mach(arg)
        
    
    

if __name__ == '__main__':
    komprimier()
    
    
        