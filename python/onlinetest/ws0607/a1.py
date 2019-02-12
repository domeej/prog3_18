'''
Created on 12.02.2019

@author: dkoeh001
'''
import sys


def highest(dic):
    top = 0
    new = {}
    for k,v in dic.items():
        if v>top:
            top=v
    
    for k,v in dic.items():
        if v == top:
            new[k] = v

    new = sorted(new.items(), key=lambda x:x[0])
    for k,v in new:
        print("{}:{}".format(v,k))
    
def readArgs(argv):
    dic = {}
    argv = argv[1:]
    
    for w in argv:
        if w in dic.keys():
            dic[w] += 1
        else:
            dic[w] = 1
    
    highest(dic)
    
if __name__ == '__main__':

    dic = readArgs(sys.argv)
    