'''
Created on 12.02.2019

@author: dkoeh001
'''

def rumdreh(s):
    return s[::-1]


def vokale(s):
    v = ""
    k = ""
    
    for c in s:
        if c.upper() in "AEIOU":
            v+= c
        else:
            k += c

    return (v,k)

def ersetze(zk, dic):
    new = zk[:]
    for k,v in dic.items():
        search = "{" + k + "}"
        new= new.replace(search, v)
    return new    

if __name__ == '__main__':
    #print(rumdreh("hallo"))
    #print(vokale("Obstbaum"))
    
    zk = "Hallo {welt} das ist {gefuehl}"
    dic = {"welt":"Scheibe", "gefuehl":"flach"}
    ersetze(zk, dic)
    