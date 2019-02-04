'''
Created on 03.02.2019

@author: domee
'''
import os, sys, datetime
os.chdir('messkram')
from random import gauss

sys.path.insert(0, '/home/domee/gitRepos/prog3_18/python/a40')
from a40 import Messreihe, Messwert

def makeMessreihe(jahr,monat,tag,anzahl):
    mue = 17.0
    sigma = 3
    i = 0
    zeitpunkt = datetime.datetime(jahr, monat, tag, 0, 0, 0)
    mr = Messreihe()
    while(i<anzahl):
        temp = gauss(mue, sigma)
        mr + Messwert("{:%Y-%m-%d %H:%M:%S.%s}".format(zeitpunkt)[:-4], temp)  
        i+=1
        zeitpunkt += datetime.timedelta(minutes=15)
    return mr
    
def messreihe2text(mr):
    for e in mr:
        yield '"'+str(e.zeitpunkt) + '",' +  '{:00.5}'.format(e.temperatur)


if __name__ == '__main__':
    mr = makeMessreihe(2020, 2, 1, 50)

    x = messreihe2text(mr)
    
    print(next(x))
    print(next(x))
    print(next(x))

    
    
    