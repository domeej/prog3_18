'''
Created on 10.02.2019

@author: domee
'''
from asyncore import read

def readFile(f):
    dic = {}
    
    for line in open(f):
        line = line.split()

        if len(line)>0:
            if line[0] not in dic.keys():
                dic[line[0]] = int(line[1]),int(line[2]), int(line[3])
    return dic

def anz_bestanden(f):
    dic = readFile(f)
    bestanden = []
    for k,v in dic.items():
        if sum(v) >=7:
            bestanden.append([k,v])
    
    return len(bestanden)

def anz_nullpunkte(f):
    dic = readFile(f)
    versagt = []
    for k,v in dic.items():
        if sum(v) ==0:
            versagt.append([k,v])
    
    return len(versagt)


def bestex(f, x=5):
    dic = readFile(f)
    sumdic = {}

    for k,v in dic.items():
        sumdic[k] = sum(v)
    
    lis = sorted(sumdic.items(), key=lambda x : x[0])
    lis =  sorted(lis, key=lambda x: x[1], reverse=True)
    return lis[:x]
    
def wer_bestanden(f):
    dic = readFile(f)
    bestanden = []
    for k,v in dic.items():
        if sum(v) >=7:
            bestanden.append(k)
    
    return bestanden

def wer_nullpunkte(f):
    dic = readFile(f)
    versagt = []
    for k,v in dic.items():
        if sum(v) ==0:
            versagt.append(k)
    return versagt
    
    
def durchschnitt_punkte_je_aufgabe(f):
    dic = readFile(f)
    res = {}
    res["1"] = 0
    res["2"] = 0
    res["3"] = 0
    
    for v in dic.values():
        res["1"] += v[0] 
        res["2"] += v[1]    
        res["3"] += v[2]

    # durchschnitt berechnen 
    teilnemherAnzahl = len(dic.values())

    res["1"] = "{:.2f}".format(res["1"] / teilnemherAnzahl)
    res["2"] = round(res["2"] / teilnemherAnzahl, 2)
    res["3"] = "{:.2f}".format(res["3"] / teilnemherAnzahl)
    
    return res
    
if __name__ == '__main__':
    f2 = "punkte2.txt"
    #print(readFile("punkte2.txt"))
    print(anz_bestanden("punkte2.txt"))
    print(anz_nullpunkte("punkte2.txt"))
    print(bestex(f2, 5))
    print(wer_bestanden(f2))
    print(wer_nullpunkte(f2))
    
    print(durchschnitt_punkte_je_aufgabe(f2))
    

    