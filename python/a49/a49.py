'''
Created on 04.02.2019

@author: domee
'''

FILENAME = "access.log"
import re

def getPerDatatype():
    JPG = "jpg"
    PNG = "png"
    GIF = "gif"
    types = [JPG, PNG, GIF]
    
    dic = {}
    for line in open(FILENAME):
        line = line.strip()
        
        for type in types:
            #print(type)
            ex = ".*GET.*\.({}).*".format(type)
            if type not in dic.keys():
                #print("nicht in dic")
                dic[type] = []
            result = re.match(ex,line)
            
            if result:
                dic[type] = dic[type] + [line]
    
    print(len(dic[JPG]))
    print(len(dic[PNG]))
    print(len(dic[GIF]))
    
    
if __name__ == '__main__':
    getPerDatatype()