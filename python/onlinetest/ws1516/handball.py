'''
Created on 05.02.2019

@author: domee
'''

def anz_spiele(fname):
    games = readFile(fname)
    return len(games)

def hoechster_heimsieg(fname):
    games = readFile(fname)
    hoechste = (max(games, key= lambda x: int(x["tore"].split(':')[0])))
    return hoechste["tore"]
    
def hoechster_auswaertssieg(fname):
    games = readFile(fname)
    hoechste = (max(games, key= lambda x: int(x["tore"].split(':')[1])))
    return hoechste["tore"]
    
def hoechster_sieg(fname):
    heimspiel = hoechster_heimsieg(fname)
    auswaerts = hoechster_auswaertssieg(fname)
    
    h1,h2 = heimspiel.split(':')
    a1,a2 = auswaerts.split(':')
    h1,h2= int(h1), int(h2)
    a1,a2= int(a1), int(a2)

    hlis = [h1,h2]
    alis = [a1,a2]
    
    res = max(hlis + alis)

    if res in (hlis):
        return "{}:{}".format(h1,h2)
    else:
        return "{}:{}".format(a1,a2)
    
    
def meister(fname):
    games = readFile(fname)
    dic = {}
    #classic
    
    for g in games:
        if g["heim"] not in dic.keys():
            dic[g["heim"]] = 0
        
        if g["gast"] not in dic.keys():
            dic[g["gast"]] = 0
    
        dic[g["heim"]] = dic[g["heim"]] +  int(g["punkte"].split(':')[0])
        dic[g["gast"]] = dic[g["gast"]] +  int(g["punkte"].split(':')[1])

    return max(dic.items(), key= lambda x: x[1])
    
def letzter(fname):
    games = readFile(fname)
    dic = {}
    #classic
    
    for g in games:
        if g["heim"] not in dic.keys():
            dic[g["heim"]] = 0
        
        if g["gast"] not in dic.keys():
            dic[g["gast"]] = 0
    
        dic[g["heim"]] = dic[g["heim"]] +  int(g["punkte"].split(':')[0])
        dic[g["gast"]] = dic[g["gast"]] +  int(g["punkte"].split(':')[1])

    return min(dic.items(), key= lambda x: x[1])

def beste_drei_tordifferenz(fname):
    games = readFile(fname)
    dic = {}
    lis = []
    print("xxxxxx")
    for g in games:
        h,a = g["tore"].split(':')
        h,a = int(h), int(a)

        if h>a:
            g["tordiff"] = h-a
        else:
            g["tordiff"] = a-h
        
        lis.append(g)
    return sorted(lis, key= lambda x: x["tordiff"], reverse=True)[:3]
        
def readFile(fname):
    games = []
    first = True
    
    for line in open(fname):
        dic= {}
        line = line.strip().split(';')
        if first:
            first = False
            
        else:
            # Nr;Datum;Zeit;Heim;Gast;Tore;Punkte
            dic["nr"] = int(line[0])
            dic["datum"] = line[1]
            dic["zeit"] = line[2]
            dic["heim"] = line[3]
            dic["gast"] = line[4]
            dic["tore"] = line[5]
            dic["punkte"] = line[6]
            games.append(dic)
    
    return games

if __name__ == '__main__':
    fname = "hb.csv"
    
    print(anz_spiele(fname))
    print(hoechster_heimsieg(fname))
    print(hoechster_auswaertssieg(fname))
    print(hoechster_sieg(fname))
    print(meister(fname))
    print(letzter(fname))
    print(beste_drei_tordifferenz(fname))
    