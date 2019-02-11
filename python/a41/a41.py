'''
Created on 03.02.2019

@author: domee
'''
import sys, statistics
sys.path.insert(0, '/home/domee/gitRepos/prog3_18/python/a40')
from a40 import Messreihe

def do():
    FILE = '../a40/messwerte.csv'
    mr = Messreihe(open(FILE, 'r'))
    
    # wie viele einträge
    print(len(mr))
    
    # min und max -> worin vorteil zu list comprehension?
    print(min(mr))
    print(max(mr))
    
    # temperatur > iwas
    print([mw for mw in mr if mw.temperatur > 19.75])
    
    # an datum 
    print([mw for mw in mr['"2019-01-11'] if mw.temperatur > 19.75])
    
    # 17 grad 
    print([mw for mw in mr if mw.temperatur >= 17 and mw.temperatur <= 18])
    
    # mittelwert
    print(statistics.mean([mw.temperatur for mw in mr]))
    
if __name__ == '__main__':
    do()