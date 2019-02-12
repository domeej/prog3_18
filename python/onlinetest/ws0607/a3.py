'''
Created on 12.02.2019

@author: dkoeh001
'''

def schuerfDic(f):
    flag = 0
    lis = []
    dic = {}
    innerdic = {}
    for line in open(f):
        line = line.split()
        
        if len(line)>0:

            content = line[0]
            if content == "BEGIN:VCARD":
                flag = 1
            if content == "END:VCARD":
                flag = 0
                lis.append(dic)
                dic = {}
            
            if(flag):
                if content not in ["BEGIN:VCARD", "END:VCARD"]:
                    k, v  = content.split(':')
                    
                    # wenn der key nochmal gesplittet werden kann
                    if len(k.split(';')) > 1:
                        print(k.split(';'))
                        for e in k.split(';'):
                            pass
                            
                    
                    print(k,v)
                    
                    
                    innerValues = v.split(';')
                    #print(k, innerValues)
                    dic[k] = v
    print(lis)

if __name__ == '__main__':
    schuerfDic("data.txt")